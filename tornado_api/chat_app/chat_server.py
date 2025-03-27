import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.escape
import os
import uuid
import json
import datetime
import logging
from collections import deque

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("chat.log"),  # 写入文件
        logging.StreamHandler(),  # 同时输出到控制台
    ],
)
logger = logging.getLogger(__name__)

# 配置
MAX_HISTORY = 100  # 最大历史消息数
UPLOAD_DIR = "static/uploads"  # 文件上传目录

# 确保上传目录存在
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

# 存储所有活跃的WebSocket连接和用户信息
active_users = {}  # {websocket: {"user_id": str, "nickname": str}}
message_history = deque(maxlen=MAX_HISTORY)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        nickname = self.get_cookie("nickname", "")
        if not nickname:
            self.redirect("/login")
        else:
            self.render("chat.html", nickname=nickname)


class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("login.html")

    def post(self):
        nickname = self.get_body_argument("nickname", "").strip()
        if not nickname:
            self.redirect("/login")
        else:
            self.set_cookie("nickname", nickname)
            self.redirect("/")


class UploadHandler(tornado.web.RequestHandler):
    async def post(self):
        file_info = self.request.files.get("file", None)
        if not file_info:
            self.set_status(400)
            return self.write({"error": "No file uploaded"})

        file = file_info[0]
        filename = file["filename"]
        content_type = file["content_type"]
        file_body = file["body"]

        # 生成唯一文件名
        ext = os.path.splitext(filename)[1]
        new_filename = f"{uuid.uuid4().hex}{ext}"

        # 使用绝对路径保存文件
        file_path = os.path.join(os.path.dirname(__file__), UPLOAD_DIR, new_filename)

        # 确保上传目录存在
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "wb") as f:
            f.write(file_body)

        self.write(
            {
                "url": f"/static/uploads/{new_filename}",
                "filename": filename,
                "content_type": content_type,
            }
        )


class ChatWebSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        self.user_id = str(uuid.uuid4())[:8]
        # 从cookie中获取昵称
        self.nickname = tornado.escape.xhtml_escape(self.get_cookie("nickname", "匿名用户"))
        active_users[self] = {"user_id": self.user_id, "nickname": self.nickname}
        self.update_user_list()

        # 发送历史消息
        for msg in message_history:
            self.write_message(json.dumps(msg))

        self.send_system_message(f"{self.nickname} 加入了聊天室")
        logger.info(f"用户加入: {self.nickname} (ID: {self.user_id})")

    def on_close(self):
        if self in active_users:
            nickname = active_users[self]["nickname"]
            del active_users[self]
            self.update_user_list()
            self.send_system_message(f"{nickname} 离开了聊天室")
            logger.info(f"用户离开: {nickname} (ID: {self.user_id})")

    def on_message(self, message):
        try:
            data = json.loads(message)

            # 设置昵称
            if data.get("type") == "set_nickname":
                new_nickname = data.get("nickname", "").strip()
                if new_nickname:
                    old_nickname = active_users[self]["nickname"]
                    active_users[self]["nickname"] = new_nickname
                    self.nickname = new_nickname
                    # 使用cookie_secret对昵称进行签名
                    self.write_message(
                        json.dumps(
                            {
                                "type": "set_cookie",
                                "name": "nickname",
                                "value": new_nickname,
                            }
                        )
                    )
                    self.update_user_list()
                    self.send_system_message(f"{old_nickname} 改名为 {new_nickname}")
                    logger.info(
                        f"用户改名: {old_nickname} -> {new_nickname} (ID: {self.user_id})"
                    )
                return

            # 私聊消息
            if data.get("type") == "private":
                target_id = data.get("target_id")
                content = data.get("content")
                if target_id and content:
                    self.send_private_message(target_id, content)
                    logger.info(
                        f"私聊消息: 从 {self.nickname} 发送给 {self.get_nickname_by_id(target_id)} - {content}"
                    )
                return

            # 普通消息
            if data.get("type") == "message" and "content" in data:
                user_info = active_users.get(self, {})
                message_data = {
                    "type": "message",
                    "user_id": user_info.get("user_id"),
                    "nickname": user_info.get("nickname"),
                    "content": data["content"],
                    "timestamp": datetime.datetime.now().strftime("%H:%M:%S"),
                    "is_private": False,
                }
                self.broadcast_message(message_data)
                message_history.append(message_data)
                logger.info(f"公共消息: {user_info.get('nickname')} - {data['content']}")

        except json.JSONDecodeError:
            logger.error(f"消息解析错误: {message}")
            pass

    def get_nickname_by_id(self, user_id):
        for user_info in active_users.values():
            if user_info["user_id"] == user_id:
                return user_info["nickname"]
        return "未知用户"

    def send_private_message(self, target_id, content):
        sender_info = active_users.get(self, {})
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")

        # 创建发送者和接收者的消息数据
        sender_msg = {
            "type": "private",
            "user_id": sender_info.get("user_id"),
            "nickname": sender_info.get("nickname"),
            "target_id": target_id,
            "content": content,
            "timestamp": timestamp,
            "direction": "outgoing",
        }

        receiver_msg = {
            "type": "private",
            "user_id": sender_info.get("user_id"),
            "nickname": sender_info.get("nickname"),
            "target_id": target_id,
            "content": content,
            "timestamp": timestamp,
            "direction": "incoming",
        }

        # 发送给发送者
        self.write_message(json.dumps(sender_msg))

        # 发送给接收者
        for conn, user_info in active_users.items():
            if user_info["user_id"] == target_id:
                conn.write_message(json.dumps(receiver_msg))
                break

        # 添加到历史记录
        message_history.append(sender_msg)

    def broadcast_message(self, message):
        for connection in active_users.keys():
            try:
                connection.write_message(json.dumps(message))
            except:
                pass

    def send_system_message(self, content):
        message = {
            "type": "system",
            "content": content,
            "timestamp": datetime.datetime.now().strftime("%H:%M:%S"),
        }
        self.broadcast_message(message)
        message_history.append(message)

    def update_user_list(self):
        user_list = [
            {"user_id": info["user_id"], "nickname": info["nickname"]}
            for info in active_users.values()
        ]

        message = {"type": "user_list", "users": user_list}
        self.broadcast_message(message)


def make_app():
    settings = {
        "static_path": os.path.join(os.path.dirname(__file__), "static"),
        "template_path": os.path.join(os.path.dirname(__file__), "templates"),
        "cookie_secret": "your_cookie_secret_here",
        "xsrf_cookies": True,  # 启用 XSRF 保护
        "debug": True,  # 开启调试模式，方便查看错误
        "static_url_prefix": "/static/",
        "static_handler_class": tornado.web.StaticFileHandler,
        "static_handler_args": {
            "path": os.path.join(os.path.dirname(__file__), "static"),
            "default_filename": "index.html",
        },
    }

    return tornado.web.Application(
        [
            (r"/", MainHandler),
            (r"/login", LoginHandler),
            (r"/upload", UploadHandler),
            (r"/websocket", ChatWebSocket),
            (
                r"/static/(.*)",
                tornado.web.StaticFileHandler,
                {"path": settings["static_path"]},
            ),
        ],
        **settings,
    )


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("聊天服务器运行在 http://localhost:8888")
    tornado.ioloop.IOLoop.current().start()
