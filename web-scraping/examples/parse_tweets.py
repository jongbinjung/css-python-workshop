import sys
import json
import pytz
from datetime import datetime
import argparse

# set up the argument parser
parser = argparse.ArgumentParser(description=(
    "Generate tab-seperated output where each row corresponds to a tweet "
    "and the columns are date, hour, minute, and timezone"))
args = parser.parse_args()

# process stdin line-by-line
for line in sys.stdin:
    line = line.rstrip('\n')

    # check for blank lines
    if line != '':
        try:
            tweet = json.loads(line)
        except:
            # print "skipped non json entry"
            continue

        # make sure that the tweet has all required fields
        if ('user' in tweet and 'created_at' in tweet):

            tz = str(tweet['user']['time_zone'])

            # only process tweets where users have specified US time-zones
            if 'US' in tz:
                tz = 'US/' + tz.split()[0]
                clean_time = datetime.strptime(tweet['created_at'],
                        '%a %b %d %H:%M:%S +0000 %Y')
                mytime = pytz.utc.localize(clean_time
                        ).astimezone(pytz.timezone(tz))
                print '\t'.join((mytime.strftime('%m/%d'),
                                 mytime.strftime('%H'),
                                 mytime.strftime('%M'),
                                 mytime.strftime('%Z')))
