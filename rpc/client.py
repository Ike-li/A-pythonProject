import xmlrpc.client

"""
客户端端：
通过 URL 连接到服务器。
使用 proxy.divide(x, y) 调用远程函数。
客户端将参数发送给服务器，服务器执行函数并将结果返回。
"""

proxy = xmlrpc.client.ServerProxy("http://localhost:9000/")
x = float(input("Enter the dividend: "))
y = float(input("Enter the divisor: "))
try:
    result = proxy.divide(x, y)
    print(f"The result is: {result}")
except Exception as e:
    print(f"An error occurred: {e}")
"""
设计理念和原理
RPC（远程过程调用）
核心理念：将远程服务（在另一台计算机上运行的函数或过程）视为本地函数。
客户端可以像调用本地函数一样调用远程服务，底层的通信细节（如网络传输）被隐藏。
工作原理：RPC 使用特定的通信协议（如 XML-RPC、JSON-RPC、gRPC 等）来封装和传输请求和响应。
客户端发起请求时，请求被序列化并发送到服务器，服务器解序列化请求，执行相应的函数，然后将结果序列化并返回给客户端。
例子：
如果有一个分布式系统中的服务 A（提供数据处理功能），另一个服务 B（需要进行数据处理），
服务 B 可以通过 RPC 调用服务 A 的函数，如 process_data()，就像调用本地函数一样。
"""
"""
REST API（代表状态转移）
核心理念：基于 HTTP 协议，通过操作资源（如 Web 网页、数据库记录等）来实现通信。
REST API 通常使用 HTTP 方法（如 GET、POST、PUT、DELETE 等）来操作资源，并使用统一的资源标识符（URI）来定位资源。
工作原理：客户端通过发送 HTTP 请求（包含 URL、请求方法、请求头和请求体）与服务器交互，
服务器根据请求方法和资源 URI 执行相应的操作，并返回响应（包含响应状态码、响应头和响应体）。
例子：
一个 Web 应用程序的 REST API 可以通过 GET /users/123 获取用户 ID 为 123 的用户信息，通过 POST /users 创建一个新用户。
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify(message="Hello, World!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
"""
"""
通信过程：
客户端发起请求，服务器接收到请求后执行函数。
函数执行结果通过网络返回给客户端。
客户端像调用本地函数一样获取结果。

RPC 的特点
封装性：RPC 将底层的网络通信细节隐藏起来，客户端无需关心如何发送和接收数据。
透明性：客户端调用远程函数的方式与调用本地函数几乎相同。
灵活性：可以在不同的语言和平台上实现RPC。
可扩展性：可以轻松地将服务分发到多个服务器上。
"""
