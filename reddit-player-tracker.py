import praw
import os

secret= os.environ['REDDIT_SECRET']
client_id=os.environ['REDDIT_CLIENT']



def authenticate(client_id, client_secret, password, user_agent, username):

	reddit = praw.Reddit(client_id=client_id,
	                     client_secret=secret,
	                     password=password,
	                     user_agent=user_agent,
	                     username=username)

	return reddit

	
