import asyncio
import time

import aiohttp
import requests


########################################################################################################################
# 实战例子：并发获取多个网站的内容
########################################################################################################################
# 定义一个异步函数，用于获取单个网站的内容
async def async_fetch(session, url):
    async with session.get(url) as response:
        # 等待响应并获取内容
        content = await response.text()
        print(f"Fetched {url}: {len(content)} bytes")
        return content


# 定义一个异步函数，用于并发获取多个网站的内容
async def async_fetch_all(urls):
    # 创建一个 aiohttp.ClientSession 对象
    async with aiohttp.ClientSession() as session:
        # 创建一个任务列表
        tasks = [async_fetch(session, url) for url in urls]
        # 并发运行所有任务
        await asyncio.gather(*tasks)


# 主函数
if __name__ == "__main__":
    # 定义要爬取的网站列表
    urls = [
        "https://www.example.com",
        "https://www.python.org",
        "https://www.baidu.com",
        "https://www.bing.com",
    ]

    start_time = time.time()

    # 创建事件循环并运行
    asyncio.run(async_fetch_all(urls))

    print(f"异步Spent time: {time.time() - start_time}")

########################################################################################################################
# 对比同步代码
########################################################################################################################


def fetch(url):
    response = requests.get(url)
    print(f"Fetched {url}: {len(response.text)} bytes")


def fetch_all(urls):
    for url in urls:
        fetch(url)


if __name__ == "__main__":
    urls = [
        "https://www.example.com",
        "https://www.python.org",
        "https://www.github.com",
        "https://www.bing.com",
    ]
    start_time = time.time()
    fetch_all(urls)
    print(f"同步Spent time: {time.time() - start_time}")
