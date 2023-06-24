import praw
import time

reddit = praw.Reddit(
    client_id="my_client_id",
    client_secret="my_client_secret",
    user_agent="my_user_agent",
)

while True:
    hot_posts = reddit.subreddit('all').hot(limit=10)
    for post in hot_posts:
        print(post.title)
    
    time.sleep(600)  # sleep for 10 minutes
