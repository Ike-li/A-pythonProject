import feedparser

SAVE_FILE = "ai_news.txt"  # 保存文件路径

# RSS订阅源列表
RSS_URLS = [
    "https://www.jiqizhixin.com/rss",
]


def fetch_rss():
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        for url in RSS_URLS:
            try:
                feed = feedparser.parse(url)
                for entry in feed.entries:
                    f.write(f"标题: {entry.title}\n")
                    f.write(f"链接: {entry.link}\n\n")
                print(f"成功获取AI资讯，已保存到 {SAVE_FILE}")
            except Exception as e:
                print(f"获取AI资讯失败: {e}")


def main():
    fetch_rss()


if __name__ == "__main__":
    main()
