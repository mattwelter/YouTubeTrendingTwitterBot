from requests_html import HTMLSession
from bs4 import BeautifulSoup as bs
from datetime import datetime, time
from dateutil.parser import parse
import youtube_trending_scraper
from time import sleep
import requests
import os, sys
import tweepy
import emoji
import lxml

auth = tweepy.OAuthHandler('———————————————————————————')
auth.set_access_token('———————————————————————————','———————————————————————————')
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)




def tweet():
    video_url = "https://www.youtube.com/feed/trending"
    # Init an HTML Session
    session = HTMLSession()

    # Get the html content
    response = session.get(video_url)

    # Execute Java-script
    response.html.render(sleep=1)

    # Create bs object to parse HTML
    soup = bs(response.html.html, "html.parser")

    # Write all HTML code into a file
    open("video.html", "w", encoding='utf8').write(response.html.html)

    with open('video.html', 'r') as f:
        contents = f.read()
        soup = bs(contents, 'lxml')

        videoTitle = soup.find("yt-formatted-string", { "class" : "ytd-video-renderer" }).text
        videoChannel = soup.find("paper-tooltip", { "class" : "ytd-channel-name" }).text
        videoViews = soup.find("span", { "class" : "ytd-video-meta-block" }).text

        print(videoTitle)
        print("".join(videoChannel.split()))
        print(videoViews)

    try:
        api.update_status(emoji.emojize(":writing_hand:") + videoTitle + "\n\n" + emoji.emojize(":bust_in_silhouette:") + "".join(videoChannel.split()) + "\n\n" + emoji.emojize(":eye:") + videoViews)
    except:
        print("This tweet is a duplicate.")
        try:
            api.update_status(emoji.emojize(":writing_hand:") + videoTitle + "\n\n" + emoji.emojize(":bust_in_silhouette:") + "".join(videoChannel.split()) + "\n\n" + emoji.emojize(":eye:") + videoViews + "\n" + "x2")
        except:
            print("This tweet is a duplicate. x2")




while True:
    tweet()
    sleep(43200)




