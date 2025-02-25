import os
import smtplib
import time
from datetime import datetime
from email.header import Header
from email.mime.text import MIMEText

from apscheduler.schedulers.background import BackgroundScheduler
from dotenv import load_dotenv

# 从.env文件中加载环境变量
load_dotenv()  # 加载 .env 文件

# 邮件配置
SENDER = os.getenv("SENDER")  # 发件人邮箱
EMAIL_AUTHORIZATION_CODE = os.getenv(
    "EMAIL_AUTHORIZATION_CODE")  # 发件人邮箱授权码（不是邮箱密码）
SMTP_SERVER = 'smtp.qq.com'  # 邮箱的SMTP服务器地址
SMTP_PORT = 587  # SMTP服务器端口
RECIPIENT = os.getenv("RECIPIENT").split(',')  # 收件人邮箱（可多个）
print(SENDER, EMAIL_AUTHORIZATION_CODE, RECIPIENT)


def send_email():
    """发送日志邮件"""
    log_content = f"正在测试发送邮件 at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

    # 创建邮件内容
    message = MIMEText(log_content, 'plain', 'utf-8')
    message['From'] = f'"Log Sender" <{SENDER}>'  # Use proper email format
    message['To'] = Header("，".join(RECIPIENT), 'utf-8')
    message['Subject'] = Header('测试发送邮件', 'utf-8')

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # 启用TLS加密
        server.login(SENDER, EMAIL_AUTHORIZATION_CODE)
        server.sendmail(SENDER, RECIPIENT, message.as_string())
        server.quit()
        print(f"Email sent successfully at {datetime.now()}")
    except Exception as e:
        print(f"Failed to send email: {e}")


def main():
    """主函数，启动后台任务"""
    # 创建后台调度器
    scheduler = BackgroundScheduler()

    # 每分钟发送一次邮件
    scheduler.add_job(send_email, 'interval', minutes=1)

    # 启动调度器
    scheduler.start()
    print("Background scheduler started. Press Ctrl+C to exit.")

    try:
        # 保持程序运行
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        # 清理资源
        scheduler.shutdown()
        print("\nScheduler stopped gracefully.")


if __name__ == "__main__":
    main()
