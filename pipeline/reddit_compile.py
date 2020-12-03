import pandas as pd 
import numpy as np 
import os 
from tqdm import tqdm 
import re
import matplotlib.pyplot as plt

#get humor data
ls = os.listdir('reddit_scrape/humor/')

df = pd.DataFrame(columns=['id','title','text','score', 'label'])
frames = [df]
for l in tqdm(ls):
	temp = pd.read_csv('reddit_scrape/humor/'+l)
	frames.append(temp)

df = pd.concat(frames)
df = df.reset_index()

#get non humor data
df2 = pd.DataFrame(columns=['id','title','text','score','label'])
frames = [df2]
ls = os.listdir('reddit_scrape/worldnews/')
for l in tqdm(ls):
	temp = pd.read_csv('reddit_scrape/worldnews/'+l)
	frames.append(temp)

df2 = pd.concat(frames)
df2 = df2.reset_index()

df3 = pd.DataFrame(columns=['id','title','text','score','label'])
frames = [df3]
ls = os.listdir('reddit_scrape/redditcom/')
for l in tqdm(ls):
	temp = pd.read_csv('reddit_scrape/redditcom/'+l)
	frames.append(temp)

df3 = pd.concat(frames)
df3 = df3.reset_index()

#set labels and concat
df['label'] = 1
df2['label'] = 0
df3['label'] = 0
df = pd.concat([df,df2, df3])

#filter
df = df[(df['score'] > 3) & (df['ratio'] > 0.75)]

print(df.describe())

#compile
df = df.replace(np.nan, '', regex=True)
df_out = pd.DataFrame(columns=['id','title','text','score'])
lens = []
for x in tqdm(range(df.shape[0])):
	temp = df.iloc[x].copy()
	#combine text and title together, skip title if text begins with title
	if not temp['text'].startswith(temp['title']):
		temp['text'] = temp['title'] + ' ' + temp['text']
	#fix weird unicode bug
	temp['text'] = temp['text'].replace('â€™', '')
	df_out = df_out.append(temp, ignore_index=True)

#export
df_out = df_out.drop('title', 1)
df_out.to_csv('humor_out.csv', index=False)
