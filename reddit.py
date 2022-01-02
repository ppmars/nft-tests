import re
import pandas as pd
pd.set_option('max_colwidth', 500)
pd.set_option('max_columns', 50)

import praw
from psaw import PushshiftAPI
# Initialize PushShift
r = praw.Reddit(client_id="7dJ3eR8d0k2p6PKSTyOfyQ",         # your client id
                               client_secret="QMyh4i5iRQF8vcaljc4DXLmhcuMMGA",      # your client secret
                               user_agent="scraper")
api = PushshiftAPI(r)

import datetime as dt
start_epoch=int(dt.datetime(2021, 8, 20).timestamp())
end_epoch=int(dt.datetime(2021, 12, 25).timestamp())

results = list(api.search_comments(before=end_epoch, after=start_epoch,
                            subreddit='nft',
                            filter=['url','author', 'title', 'subreddit'],
                            limit=10000))

count = 0
for submission in results:
    # print(dt.datetime.fromtimestamp(submission.created))
    if "I am a bot" not in submission.body:
        if re.search("beeple", submission.body, re.IGNORECASE):
            count += 1
print(count)
print('{} submissions'.format(len(results)))