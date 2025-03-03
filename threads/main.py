import concurrent.futures
import threading
import time


########################################################################################################################
# 创建线程
########################################################################################################################
def worker():
    """线程执行的函数"""
    print(f"线程 {threading.current_thread().name} 开始工作...")

    # 模拟耗时操作
    time.sleep(2)
    print(f"线程 {threading.current_thread().name} 完成工作！")


# 创建线程
thread = threading.Thread(target=worker, name="MyThread")

# 启动线程
thread.start()

# 等待线程完成（可选）
thread.join()
print("主线程结束！")


########################################################################################################################
# 线程的参数
########################################################################################################################
def worker(arg1, arg2):
    print(f"线程 {threading.current_thread().name} 收到参数: {arg1}, {arg2}")


# 创建线程并传递参数
thread = threading.Thread(target=worker, args=("hello", "world"), name="MyThread")
thread.start()

########################################################################################################################
# 线程同步
########################################################################################################################
lock = threading.Lock()
counter = 0


def increment():
    global counter
    lock.acquire()  # 获取锁
    try:
        counter += 1
        print(f"线程 {threading.current_thread().name}: counter = {counter}")
    finally:
        lock.release()  # 释放锁


# 创建多个线程
threads = []
for i in range(5):
    t = threading.Thread(target=increment, name=f"Thread-{i}")
    threads.append(t)
    t.start()

# 等待所有线程完成
for t in threads:
    t.join()

########################################################################################################################
# 线程池
########################################################################################################################


def worker(n):
    print(f"线程 {threading.current_thread().name} 正在处理任务: {n}")
    return n * 2


with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    results = executor.map(worker, range(5))

print("所有任务完成！")
