"""
单例模式是一种设计模式，确保一个类只有一个实例，提供全局访问该实例的点，方便在任何地方使用；避免重复创建实例，节省内存和系统资源。
实际例子：数据库连接池管理
假设我们要管理数据库连接，希望整个应用中只有一份数据库连接实例，避免频繁创建和销毁连接，提高性能。
"""
import threading
import time


class Database:
    """
    通过__new__方法实现单例模式
    """
    _instance = None
    _lock = threading.Lock()  # 添加一个锁对象

    def __new__(cls):
        # 使用双重校验锁机制减少锁的使用次数，提高性能
        if not cls._instance:  # 第一次检查不加锁，是为了避免每次都加锁，提升性能
            with cls._lock:  # 进入临界区，在创建实例时加锁，确保同一时间只有一个线程可以进入实例化逻辑。
                if not cls._instance:  # 第二次检查是为了确保实例确实没有被创建，避免多线程再次创建实例
                    print("正在创建数据库连接...")
                    time.sleep(2)  # 模拟创建连接需要时间
                    cls._instance = super().__new__(cls)
        return cls._instance

    def connect(self):
        print("连接到数据库成功！")


# 测试：使用多线程测试单例
def test_database():
    db = Database()
    db.connect()


# 创建多个线程同时获取数据库实例
threads = []
for _ in range(10):
    thread = threading.Thread(target=test_database)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()


class Singleton:
    """
    通过__new__方法实现单例模式
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        # 如果实例不存在，创建一个实例
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)

        # 返回唯一实例
        return cls._instance


# 使用示例
s1 = Singleton()
s2 = Singleton()
assert s1 is s2


def singleton(cls):
    """
    通过装饰器实现单例模式
    """
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class MySingleton:
    """
    通过装饰器实现单例模式
    """
    pass


# 使用示例
s1 = MySingleton()
s2 = MySingleton()
assert s1 is s2


class SingletonMeta(type):
    """
    通过元类实现单例模式，适用于需要控制类的创建过程的场景。
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    """
    通过元类实现单例模式
    """
    pass


# 使用示例
s1 = Singleton()
s2 = Singleton()
assert s1 is s2
