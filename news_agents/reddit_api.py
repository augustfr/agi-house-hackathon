import praw
import time
from environs import Env

env = Env()
env.read_env()

reddit = praw.Reddit(
    client_id=env("REDDIT_CLIENT_ID", ""),
    client_secret=env("REDDIT_CLIENT_SECRET", ""),
    user_agent=env("REDDIT_USER_AGENT", ""),
)


while True:
    hot_posts = reddit.subreddit("all").hot(limit=10)
    for post in hot_posts:
        print(post.title)

    time.sleep(600)  # sleep for 10 minutes
