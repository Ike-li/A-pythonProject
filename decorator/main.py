import datetime
import time


def wrapper(func):
    # 打印出函数运行所耗时间
    def inner(*arg, **kwargs):
        start_at = datetime.datetime.now()
        result = func(start_at, *arg, **kwargs)
        end_at = datetime.datetime.now()
        print(end_at - start_at)
        return result

    return inner


@wrapper
def f(start):
    print(f"开始时间：{start}")
    time.sleep(1)
    print(f"结束时间：{datetime.datetime.now()}")


f()
