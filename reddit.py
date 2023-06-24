from dotenv import load_dotenv
import os
import praw

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT"),
)


while True:
    hot_posts = reddit.subreddit("all").hot(limit=10)
    for post in hot_posts:
        print(post.title)

    time.sleep(600)  # sleep for 10 minutes
