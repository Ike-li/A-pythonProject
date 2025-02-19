import threading
import time


def worker():
    """线程执行的函数"""
    print(f"线程 {threading.current_thread().name} 开始工作...")
    time.sleep(2)  # 模拟耗时操作
    print(f"线程 {threading.current_thread().name} 完成工作！")


# 创建线程
thread = threading.Thread(target=worker, name="MyThread")

# 启动线程
thread.start()

# 等待线程完成（可选）
thread.join()
print("主线程结束！")
