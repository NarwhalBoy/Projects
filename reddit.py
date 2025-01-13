import praw
import pandas

# Read-only instance
reddit_read_only = praw.Reddit(client_id="5fZoLxdl0hgjf3WMZ5t4cA",         # your client id
                               client_secret="3HlPRW_eHQpG1nwIFJAeKrkZ18ZOAw",      # your client secret
                               user_agent="Red Scaping")        # your user agent

subreddit = reddit_read_only.subreddit("movies")

# print("Display Name:", subreddit.display_name)
# print("Title:", subreddit.title)
# print("Description:", subreddit.description)

# for post in subreddit.top(time_filter = "all", limit = 5):
#     print(post.title, "\n")

pandas.set_option('display.max_columns', None)  # Show all columns
pandas.set_option('display.max_rows', None)     # Show all rows
pandas.set_option('display.max_colwidth', 50) # Don't truncate column text

posts = subreddit.top(time_filter = "week")
posts_dict = {"Title": [], "Post Text": [], "Post URL": []}

for post in posts:
    if ("Trailer" in post.title):
        posts_dict["Title"].append(post.title)
        posts_dict["Post Text"].append(post.selftext)
        posts_dict["Post URL"].append(post.url)


top_posts = pandas.DataFrame(posts_dict)
print(top_posts)
