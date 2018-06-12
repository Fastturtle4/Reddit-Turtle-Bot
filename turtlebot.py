# Turtle Bot
# This is a reddit bot that will monitor the subreddit reddit.com/r/turtles
# Anytime it detects the string !turtle in a comment, it will search google and post a turtle picture

import praw

# create reddit instance and select /r/turtles
reddit = praw.Reddit('turtbot')
subreddit = reddit.subreddit('learnpython')

# get the top 10 "hot" submissions
for submission in subreddit.hot(limit=5):
	print("Title: ", submission.title)
	print("Text: ", submission.selftext)
	print("Score: ", submission.score)
	print("------------------------------\n")
