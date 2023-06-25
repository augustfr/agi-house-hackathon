import feedparser
import trafilatura

class FeedReader:
    def __init__(self, url):
        self.url = url
        self.feed = feedparser.parse(self.url)

    def read_article(self, index):
        article_url = self.feed.entries[index].link
        try:
            downloaded = trafilatura.fetch_url(article_url)
            text = trafilatura.extract(downloaded)
            return {
                "metadata": self.feed.entries[index],
                "body": text,
            }
        except Exception as e:
            return {
                "error": str(e),
            }

reader = FeedReader('http://feeds.bbci.co.uk/news/rss.xml')
print(reader.feed)
article = reader.read_article(0)  # Get the first article.
if "error" not in article:
    print(article["body"])  # Print the article's body.
else:
    print("An error occurred:", article["error"])

