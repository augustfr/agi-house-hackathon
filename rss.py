import feedparser

# URL of the RSS Feed
feed_url = "http://feeds.bbci.co.uk/news/rss.xml"

# Parse the feed
feed = feedparser.parse(feed_url)

# Print each post
for entry in feed.entries:
    print("Title: ", entry.title)
    print("Link: ", entry.link)
    print("Published: ", entry.published)
    print("Summary: ", entry.summary)
    print("---" * 20)
