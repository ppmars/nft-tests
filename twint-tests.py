import csv
import datetime
import os
import re
import sys

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

output_file = 'output.csv'

def countMentions(phrase, file):
    rowcount = 0
    mentioncount = 0
    # make sure field limit is increased
    csv.field_size_limit(sys.maxsize)
    with open(file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            print('result {}: {}'.format(rowcount, row[10]))
            rowcount += 1
            if re.search(phrase, row[10], re.IGNORECASE):
                print(color.BOLD + 'mention {}: {}'.format(mentioncount, row[10]) + color.END)
                mentioncount += 1
        print('{} rows'.format(rowcount))
        print('{} mentions'.format(mentioncount))

import twint

c = twint.Config()

c.Username = "garyvee"
c.Show_hashtags = False
c.Limit = 1000
c.Store_csv = True
c.Output = output_file
c.Since = '2021-12-3 00:00:00'
c.Until ='2021-12-5 00:00:00'
c.Retweets = True

twint.run.Search(c)

countMentions("veefriends", output_file)
# os.remove(output_file)
os.truncate(output_file, 0)