document.addEventListener("DOMContentLoaded", function() {
    // DOM 元素
    const messagesContainer = document.getElementById("messages");
    const messageInput = document.getElementById("messageInput");
    const sendButton = document.getElementById("sendButton");
    const userList = document.getElementById("userList");
    const userCount = document.getElementById("userCount");
    const currentNickname = document.getElementById("currentNickname");
    const changeNicknameBtn = document.getElementById("changeNickname");
    const nicknameModal = document.getElementById("nicknameModal");
    const newNicknameInput = document.getElementById("newNickname");
    const confirmNicknameBtn = document.getElementById("confirmNickname");
    const cancelNicknameBtn = document.getElementById("cancelNickname");
    const emojiButton = document.getElementById("emojiButton");
    const uploadButton = document.getElementById("uploadButton");
    const fileInput = document.getElementById("fileInput");

    // 简单的emoji列表
    const commonEmojis = ["😀", "😃", "😄", "😁", "😅", "😂", "🤣", "😊", "😇", "🙂", "🙃", "😉", "😌", "😍", "🥰", "😘", "😗", "😙", "😚", "😋"];

    let currentUserId = null;
    let privateChatTarget = null;

    // 建立WebSocket连接
    const socket = new WebSocket("ws://" + window.location.host + "/websocket");

    // WebSocket 事件处理
    socket.onopen = function() {
        console.log("WebSocket连接已建立");
    };

    socket.onclose = function() {
        console.log("WebSocket连接已关闭");
        addSystemMessage("与服务器的连接已断开");
    };

    socket.onerror = function(error) {
        console.error("WebSocket错误:", error);
    };

    socket.onmessage = function(event) {
        try {
            const data = JSON.parse(event.data);

            switch(data.type) {
                case "message":
                    addMessage(data);
                    break;
                case "private":
                    addPrivateMessage(data);
                    break;
                case "system":
                    addSystemMessage(data.content, data.timestamp);
                    break;
                case "user_list":
                    updateUserList(data.users);
                    break;
                case "set_cookie":
                    // 处理昵称更改
                    document.cookie = `${data.name}=${data.value}; path=/`;
                    currentNickname.textContent = data.value;
                    break;
                default:
                    console.log("未知消息类型:", data);
            }
        } catch (error) {
            console.error("消息解析错误:", error);
        }
    };

    // 添加普通消息
    function addMessage(data) {
        const messageElement = document.createElement("div");
        messageElement.className = `message ${data.is_private ? "private-message" : "user-message"}`;

        let contentHtml = data.content;
        // 检查是否是图片链接
        if (data.content.match(/\.(jpeg|jpg|gif|png)$/i)) {
            contentHtml = `<img src="${data.content}" class="message-image" alt="图片">`;
        }
        // 检查是否是文件链接
        else if (data.content.startsWith("http") && data.content.includes("/static/uploads/")) {
            const filename = data.content.split("/").pop();
            contentHtml = `<a href="${data.content}" target="_blank" class="message-file">下载文件: ${filename}</a>`;
        }

        messageElement.innerHTML = `
            <div class="message-header">
                <span>${data.nickname || "匿名用户"}</span>
                <span class="message-time">${data.timestamp}</span>
            </div>
            <div class="message-content">${contentHtml}</div>
        `;

        messagesContainer.appendChild(messageElement);
        scrollToBottom();
    }

    // 添加私聊消息
    function addPrivateMessage(data) {
        const messageElement = document.createElement("div");
        messageElement.className = `message private-message`;

        let directionText = "";
        if (data.direction === "incoming") {
            directionText = `(私聊来自 ${data.nickname})`;
        } else {
            directionText = `(私聊给 ${getNicknameById(data.target_id)})`;
        }

        messageElement.innerHTML = `
            <div class="message-header">
                <span>${data.nickname} ${directionText}</span>
                <span class="message-time">${data.timestamp}</span>
            </div>
            <div class="message-content">${data.content}</div>
        `;

        messagesContainer.appendChild(messageElement);
        scrollToBottom();
    }

    // 添加系统消息
    function addSystemMessage(content, timestamp = null) {
        const messageElement = document.createElement("div");
        messageElement.className = "message system-message";

        const timeText = timestamp || new Date().toLocaleTimeString([], {hour: '2-digit', minute:'2-digit', second:'2-digit'});

        messageElement.innerHTML = `
            <div class="message-header">
                <span>系统消息</span>
                <span class="message-time">${timeText}</span>
            </div>
            <div>${content}</div>
        `;

        messagesContainer.appendChild(messageElement);
        scrollToBottom();
    }

    // 更新用户列表
    function updateUserList(users) {
        userList.innerHTML = "";
        userCount.textContent = users.length;

        users.forEach(user => {
            const userElement = document.createElement("div");
            userElement.className = "user-item";
            if (privateChatTarget === user.user_id) {
                userElement.classList.add("private");
            }

            // 显示用户昵称
            const nicknameSpan = document.createElement("span");
            nicknameSpan.className = "user-nickname";
            nicknameSpan.textContent = user.nickname || "匿名用户";
            userElement.appendChild(nicknameSpan);

            userElement.dataset.userId = user.user_id;
            userElement.dataset.nickname = user.nickname;

            userElement.addEventListener("click", function() {
                const userId = this.dataset.userId;
                const nickname = this.dataset.nickname;

                if (privateChatTarget === userId) {
                    // 取消私聊
                    privateChatTarget = null;
                    document.querySelectorAll(".user-item").forEach(item => {
                        item.classList.remove("private");
                    });
                    addSystemMessage(`已退出与 ${nickname} 的私聊模式`);
                } else {
                    // 开始私聊
                    privateChatTarget = userId;
                    document.querySelectorAll(".user-item").forEach(item => {
                        item.classList.remove("private");
                    });
                    this.classList.add("private");
                    addSystemMessage(`已进入与 ${nickname} 的私聊模式`);
                }
            });

            userList.appendChild(userElement);
        });
    }

    // 根据用户ID获取昵称
    function getNicknameById(userId) {
        const userItem = document.querySelector(`.user-item[data-user-id="${userId}"]`);
        return userItem ? userItem.dataset.nickname : "未知用户";
    }

    // 滚动到底部
    function scrollToBottom() {
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }

    // 发送消息
    function sendMessage() {
        const content = messageInput.value.trim();
        if (!content) return;

        if (privateChatTarget) {
            // 发送私聊消息
            socket.send(JSON.stringify({
                type: "private",
                target_id: privateChatTarget,
                content: content
            }));
        } else {
            // 发送普通消息
            socket.send(JSON.stringify({
                type: "message",
                content: content
            }));
        }

        messageInput.value = "";
    }

    // 上传文件
    function uploadFile(file) {
        if (!file) return;

        const formData = new FormData();
        formData.append("file", file);
        formData.append("_xsrf", getCookie("_xsrf"));  // 添加 XSRF 令牌

        fetch("/upload", {
            method: "POST",
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.url) {
                // 发送文件消息
                if (privateChatTarget) {
                    socket.send(JSON.stringify({
                        type: "private",
                        target_id: privateChatTarget,
                        content: data.url
                    }));
                } else {
                    socket.send(JSON.stringify({
                        type: "message",
                        content: data.url
                    }));
                }
            }
        })
        .catch(error => {
            console.error("上传错误:", error);
            addSystemMessage("文件上传失败");
        });
    }

    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(';').shift();
    }

    // 事件监听
    sendButton.addEventListener("click", sendMessage);

    messageInput.addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            sendMessage();
        }
    });

    // 更改昵称
    changeNicknameBtn.addEventListener("click", function() {
        newNicknameInput.value = currentNickname.textContent;
        nicknameModal.style.display = "flex";
        newNicknameInput.focus();
    });

    confirmNicknameBtn.addEventListener("click", function() {
        const newNickname = newNicknameInput.value.trim();
        if (newNickname) {
            socket.send(JSON.stringify({
                type: "set_nickname",
                nickname: newNickname
            }));
            nicknameModal.style.display = "none";
        }
    });

    cancelNicknameBtn.addEventListener("click", function() {
        nicknameModal.style.display = "none";
    });

    // Emoji 选择器
    let emojiPickerVisible = false;
    const emojiPicker = document.createElement("div");
    emojiPicker.className = "emoji-picker";
    emojiPicker.style.display = "none";
    document.body.appendChild(emojiPicker);

    // 创建emoji按钮
    commonEmojis.forEach(emoji => {
        const button = document.createElement("button");
        button.textContent = emoji;
        button.className = "emoji-button";
        button.addEventListener("click", () => {
            messageInput.value += emoji;
            emojiPicker.style.display = "none";
            messageInput.focus();
        });
        emojiPicker.appendChild(button);
    });

    emojiButton.addEventListener("click", function() {
        emojiPickerVisible = !emojiPickerVisible;
        emojiPicker.style.display = emojiPickerVisible ? "grid" : "none";
    });

    // 点击其他地方关闭emoji选择器
    document.addEventListener("click", function(event) {
        if (!emojiPicker.contains(event.target) && !emojiButton.contains(event.target)) {
            emojiPicker.style.display = "none";
        }
    });

    // 文件上传
    uploadButton.addEventListener("click", function() {
        fileInput.click();
    });

    fileInput.addEventListener("change", function() {
        if (fileInput.files.length > 0) {
            uploadFile(fileInput.files[0]);
            fileInput.value = "";
        }
    });

    // 点击模态框外部关闭
    nicknameModal.addEventListener("click", function(event) {
        if (event.target === nicknameModal) {
            nicknameModal.style.display = "none";
        }
    });

    // 初始欢迎消息
    addSystemMessage("欢迎来到 Tornado 在线聊天室！");
});
