"""
Script to download episodes of The News Quiz when they are available via the
BBC Friday Night Comedy podcast.
Currently running on my pythonanywhere.com box.
"""

import os
import datetime
import urllib
from bs4 import BeautifulSoup


def dl(url, filename):
    """download mp3 file using urllib.urlretrieve"""
    print "Downloading {0} from {1}".format(filename, url)
    urllib.urlretrieve(url, filename)
    print "Downloading complete"


def check_rss(url):
    """check rss feed for News Quiz episodes"""
    feed = urllib.urlopen(url).read()
    soup = BeautifulSoup(feed, 'html.parser')
    item = soup.find('item') #find first item tag in feed

    title = str(item.title.string).lower()
    link = str(item.link.string)

    mp3_title = title.replace('fricomedy:  ', '').replace(' ', '_') + '.mp3'

    #download mp3 if title tag string contains 'the news quiz'
    if (title.find('the news quiz')):
        dl(link, mp3_title)


today = datetime.date.today()
weekday = today.weekday()

# If Monday run check_rss
if (weekday == 0):
    #change dir for pythonanywhere purposes
    os.chdir('/home/richyvk/Friday-night-comedy-downloader/')
    check_rss('http://www.bbc.co.uk/programmes/p02pc9pj/episodes/downloads.rss')
else:
    print "No download today, it's not Monday"
