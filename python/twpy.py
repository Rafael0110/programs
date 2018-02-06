#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Tweepyライブラリをインポート
import tweepy
import urllib
import copy
import os

# 各種キーをセット
CONSUMER_KEY = 'WQw5XnD0EIVNj3AuT5m6ijiM6'
CONSUMER_SECRET = 'PJV59MHqotZg8IjcGqzqMmrd5YOQoWyWWuNTbXDhFlGiB9T8nR'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
ACCESS_TOKEN = '232266833-muorp5MOVJNVop2ifUEsHQBJ45sZLCHDe8RAH6mb'
ACCESS_SECRET = 's6Z8Us7apm9ZXekmrodwxKcjcR7btgtEVrZrSWqwHz4Il'
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

#APIインスタンスを作成
api = tweepy.API(auth)

# これだけで、Twitter APIをPythonから操作するための準備は完了。
print('Done!')

# print api.home_timeline()[0].text
# api.home_timeline()[0]
# api.update_status(status='オッス！ from Tweepy')
# search_result = api.search(q='安倍')

# names = {"monkey":"monkeydaichan"}
names = {"araco_h":0}
 
for twi_id,tweet_id in names.items():
	sinceid			= api.user_timeline(twi_id).max_id
	maxid				= api.user_timeline(twi_id).max_id
	maxid_init	= 0
	folder			= "./" + twi_id + "/"

	if os.path.exists(folder) == False :
		os.makedirs(folder)

	elif os.path.exists(folder+'tweet_id') :
		with open(folder + 'tweet_id','r') as f:
			print "read maxid"
			sinceid				= int(f.readline())
			maxid					= int(f.readline())
			sinceid_init	= copy.deepcopy(sinceid)
			maxid_init		= copy.deepcopy(maxid)

	print " " + twi_id + " start download mediafile"
	for l in range(16):
		for twi in api.user_timeline(twi_id, count=200, max_id=maxid, include_rts=False):
			if hasattr(twi, "extended_entities"):
				if twi.extended_entities.has_key("media"):
					for index,media in enumerate(twi.extended_entities["media"]):
						if media["type"] == 'video' :
							bit = 0
							ind = 0
							for index,video in enumerate(media["video_info"]["variants"]):
								if 'bitrate' in video.keys() :
									if bit < video["bitrate"] :
										bit = video["bitrate"]
										ind = index
							img_url = media["video_info"]["variants"][ind]['url']
							print("\t  " + str(media["id"]) + " video save to " + folder + "")
							urllib.urlretrieve(media["video_info"]["variants"][ind]['url'],os.path.basename(img_url))
						else :
							img_url = media["media_url_https"]
							print("\t" + str(media["id"]) + " image save to " + folder)
							img = urllib.urlopen(img_url)
							tmp_path = open(folder + os.path.basename(img_url), "wb")
							tmp_path.write(img.read())
							img.close()
							tmp_path.close()
			maxid = twi.id

	with open(folder + 'tweet_id','w') as f:
		if maxid_init != maxid :
			print "write maxid"
			f.write(str(maxid))
		else :
			print "write 0"
			f.write(str(0))