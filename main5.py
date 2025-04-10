import struct
import socket
import logging

# 配置日志输出
logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")

# 全局配置
RECEIVER_MAC = "AA:BB:CC:DD:EE:FF"
RECEIVER_IP = "10.0.0.1"
RECEIVER_PORT = 5678


# ========================= 发送端 =========================#
def application_layer_send(data):
    """应用层：生成原始数据（如HTTP请求）"""
    logging.info(f"\n[应用层] 生成数据: {data}")
    return data.encode("utf-8")


def calculate_checksum(data):
    """计算校验和"""
    if len(data) % 2 == 1:
        data += b"\0"
    words = struct.unpack("!%dH" % (len(data) // 2), data)
    checksum = sum(words)
    checksum = (checksum >> 16) + (checksum & 0xFFFF)
    checksum = checksum + (checksum >> 16)
    return ~checksum & 0xFFFF


def transport_layer_encapsulate(payload, src_port, dst_port):
    """传输层：封装TCP头部"""
    window = 65535
    tcp_header = struct.pack(
        "!HHLLBBHHH",
        src_port,  # 源端口
        dst_port,  # 目的端口
        1000,  # 序列号
        0,  # 确认号
        5 << 4,  # 数据偏移
        0,  # 标志位
        window,  # 窗口大小
        0,  # 校验和
        0,  # 紧急指针
    )
    pseudo_header = struct.pack(
        "!4s4sBBH",
        socket.inet_aton("192.168.1.2"),  # 源IP
        socket.inet_aton(RECEIVER_IP),  # 目的IP
        0,  # 保留字节
        6,  # 协议号(TCP)
        len(tcp_header) + len(payload),  # TCP长度
    )
    checksum_data = pseudo_header + tcp_header + payload
    checksum = calculate_checksum(checksum_data)

    # 重新打包TCP头部，包含校验和
    tcp_header = struct.pack(
        "!HHLLBBHHH", src_port, dst_port, 1000, 0, 5 << 4, 0, window, checksum, 0
    )
    logging.info(f"[传输层] 添加TCP头 | 源端口: {src_port} 目的端口: {dst_port} 校验和: {checksum}")
    return tcp_header + payload


def network_layer_encapsulate(payload, src_ip, dst_ip):
    """网络层：封装IP头部"""
    ip_header_len = 5
    total_len = ip_header_len * 4 + len(payload)
    ip_header = struct.pack(
        "!BBHHHBBH4s4s",
        (4 << 4) + ip_header_len,  # 版本号和头部长度
        0,  # 服务类型
        total_len,  # 总长度
        54321,  # 标识
        0,  # 标志和片偏移
        64,  # TTL
        6,  # 协议(TCP)
        0,  # 校验和
        socket.inet_aton(src_ip),  # 源IP
        socket.inet_aton(dst_ip),  # 目的IP
    )

    # 计算IP头部校验和
    checksum = calculate_checksum(ip_header)

    # 重新打包IP头部，包含校验和
    ip_header = struct.pack(
        "!BBHHHBBH4s4s",
        (4 << 4) + ip_header_len,
        0,
        total_len,
        54321,
        0,
        64,
        6,
        checksum,
        socket.inet_aton(src_ip),
        socket.inet_aton(dst_ip),
    )
    logging.info(f"[网络层] 添加IP头 | 源IP: {src_ip} 目的IP: {dst_ip} 校验和: {checksum}")
    return ip_header + payload


def data_link_layer_encapsulate(payload, src_mac, dst_mac):
    """数据链路层：封装以太网帧"""
    dst_mac_bytes = bytes.fromhex(dst_mac.replace(":", ""))
    src_mac_bytes = bytes.fromhex(src_mac.replace(":", ""))
    eth_type = b"\x08\x00"  # IPv4类型
    frame = dst_mac_bytes + src_mac_bytes + eth_type + payload
    logging.info(f"[数据链路层] 添加MAC头 | 源MAC: {src_mac} 目的MAC: {dst_mac}")
    return frame


def physical_layer_send(frame):
    """物理层：将帧转换为比特流（模拟）"""
    logging.info(f"[物理层] 转换为比特流并发送（长度: {len(frame)} bytes）")
    return frame  # 实际中可能添加调制/编码逻辑


# ========================= 接收端 =========================#
def physical_layer_receive(bitstream):
    """物理层：接收比特流"""
    logging.info(f"\n[物理层] 接收到比特流（长度: {len(bitstream)} bytes）")
    return bitstream


def data_link_layer_decapsulate(frame):
    """数据链路层：解析MAC头部"""
    dst_mac = ":".join(f"{b:02x}" for b in frame[:6])
    src_mac = ":".join(f"{b:02x}" for b in frame[6:12])
    # eth_type = frame[12:14]
    payload = frame[14:]
    logging.info(f"[数据链路层] 解析MAC头 | 源MAC: {src_mac} 目的MAC: {dst_mac}")
    return payload


def network_layer_decapsulate(packet):
    """网络层：解析IP头部"""
    dst_ip = socket.inet_ntoa(packet[16:20])
    payload = packet[20:]
    logging.info(f"[网络层] 解析IP头 | 目的IP: {dst_ip}")
    return payload


def transport_layer_decapsulate(segment):
    """传输层：解析TCP头部"""
    dst_port = struct.unpack("!H", segment[2:4])[0]
    payload = segment[20:]  # 简化处理，固定TCP头长度为20字节
    logging.info(f"[传输层] 解析TCP头 | 目的端口: {dst_port}")
    return payload


def application_layer_receive(payload):
    """应用层：处理最终数据"""
    data = payload.decode("utf-8")
    logging.info(f"[应用层] 接收数据: {data}")
    return data


# ========================= 模拟运行 =========================#
def simulate_network_communication():
    # 发送端封装过程
    app_data = "GET /index.html HTTP/1.1"
    payload = application_layer_send(app_data)
    tcp_segment = transport_layer_encapsulate(payload, 1234, RECEIVER_PORT)
    ip_packet = network_layer_encapsulate(tcp_segment, "192.168.1.2", RECEIVER_IP)
    frame = data_link_layer_encapsulate(ip_packet, "00:11:22:33:44:55", RECEIVER_MAC)
    bitstream = physical_layer_send(frame)

    # 模拟网络传输（直接传递比特流）
    received_bitstream = bitstream

    # 接收端解封装过程
    received_frame = physical_layer_receive(received_bitstream)
    ip_packet = data_link_layer_decapsulate(received_frame)
    tcp_segment = network_layer_decapsulate(ip_packet)
    app_payload = transport_layer_decapsulate(tcp_segment)
    final_data = application_layer_receive(app_payload)

    return final_data


if __name__ == "__main__":
    result = simulate_network_communication()
    print("\n最终接收到的数据:", result)
