import logging
from xmlrpc.server import SimpleXMLRPCServer

"""
服务器端：
定义了一个 divide 函数。
创建了一个 RPC 服务器，监听本地主机的 9000 端口。
将 divide 函数注册为可远程调用的函数。
"""


def divide(x, y):
    """计算两个数字的除法"""
    return x / y


logging.basicConfig(level=logging.INFO)
server = SimpleXMLRPCServer(("localhost", 9000))
server.register_function(divide, "divide")
logging.info("Serving XML-RPC on localhost port 9000")
server.serve_forever()
