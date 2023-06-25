import feedparser
import trafilatura

class FeedReader:
    def __init__(self, feed_url=None):
        self.feed_url = feed_url
        self.feed = None

    def set_feed(self, feed_url):
        self.feed_url = feed_url
        self.feed = None

    def get_feed_entries(self):
        if self.feed_url is None:
            return {"error": "No feed URL set"}

        try:
            self.feed = feedparser.parse(self.feed_url)
        except Exception as e:
            return {"error": str(e)}

        entries = []
        for entry in self.feed.entries:
            entries.append({
                "Title": entry.title,
                "Link": entry.link,
                "Published": entry.published,
                "Summary": entry.summary
            })

        return entries

    def get_plain_text(self, url):
        try:
            downloaded = trafilatura.fetch_url(url)
            return trafilatura.extract(downloaded)
        except Exception as e:
            return {"error": str(e)}

# Create a new FeedReader instance and specify the feed URL
reader = FeedReader("http://feeds.bbci.co.uk/news/rss.xml")

# Get entries from the feed
entries = reader.get_feed_entries()
if 'error' not in entries:
    # Get the plain text of the first article
    plain_text = reader.get_plain_text(entries[0]['Link'])

    # Check if an error occurred
    if 'error' in plain_text:
        print('An error occurred:', plain_text['error'])
    else:
        print(plain_text)
else:
    print('An error occurred:', entries['error'])

