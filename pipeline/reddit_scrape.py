import pandas as pd 

import praw
from psaw import PushshiftAPI

import datetime as dt
import random
from tqdm import tqdm
import os 

r = praw.Reddit(client_id="uYIHqEkLBqDUxg", client_secret="aVjbqIzEFpUd1q6G7XbepC6d38g",
                      password="", user_agent="comment_read",
                      username="")
api = PushshiftAPI(r)

#check for existing files
dic = []
ls = os.listdir('reddit_scrape')
for l in ls:
	print(l[:-4])
	dic.append(l[:-4])

#run in a loop
for x in tqdm(range(1000)):
	#pick a random day
	year = random.randint(2005,2011)
	month = random.randint(1,12)
	day = random.randint(1,29)
	if month == 2:
		day = min(day, 27)
	start_epoch=int(dt.datetime(year, month, day).timestamp())
	end_epoch=int(dt.datetime(year, month, day+1).timestamp())
	#get the posts for that day from the determined subreddit
	if start_epoch not in dic:
		dic.append(start_epoch)
		posts = list(api.search_submissions(
									after=start_epoch,
									before=end_epoch,
		                            subreddit='reddit.com',
		                            filter=['url','author', 'title', 'subreddit'],
		                            mod_removed=True,
		                            user_removed=True,
		                            limit=None))
		df = pd.DataFrame(columns=['id','title','text','score'])
		for post in posts:
			try:
				df = df.append({'id':post.id, 'title':post.title,'text':post.selftext,'score':post.score,'ratio':post.upvote_ratio}, ignore_index=True)
			except:
				break

		#df = df.reset_index()
		df = df[df['text'] != '[removed]']
		df = df[df['text'] != '[deleted]']

		df.to_csv('reddit_scrape/'+str(start_epoch)+'.csv', index=False)