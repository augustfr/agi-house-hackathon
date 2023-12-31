import feedparser
import trafilatura


class FeedReader:
    def __init__(self, url):
        self.url = url
        feed = feedparser.parse(self.url)
        self.feed = [
            {
                key: entry.get(key, None)
                for key in ["title", "summary", "link", "published"]
            }
            for entry in feed.entries
        ]

    def read_article(self, index):
        try:
            article_url = self.feed[index]["link"]
            downloaded = trafilatura.fetch_url(article_url)
            text = trafilatura.extract(downloaded)
            return {
                "metadata": self.feed[index],
                "body": text,
            }
        except Exception as e:
            return {
                "error": str(e),
            }
        

reader = FeedReader("http://feeds.bbci.co.uk/news/rss.xml")
# article = reader.read_article(0)  # Get the first article.
# if "error" not in article:
#     print(article["body"])  # Print the article's body.
# else:
#     print("An error occurred:", article["error"])
#The broadcasters just finished this story: {news_story_script}\n\nWrite an engaging transition for the anchor to start talking about the new topic. Make sure it is a smooth change from the previous story to the new one. Here is the title and summary of the next topic: \n{next_topic}