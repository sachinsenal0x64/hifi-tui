import podsearch
import feedparser
import json

input = input(" ")

podcasts = podsearch.search(input, country="us", limit=10)

url = podcasts[0].feed

print(url)


def fetch_rss_data(url):
    feed = feedparser.parse(url)
    for entry in feed.entries:
        print("Entry Title:", entry.title)
        print("Entry Link:", entry.link)
        print("Entry Published Date:", entry.published)
        print("Entry Summary:", entry.summary)
        enclosure = entry.enclosures
        print(enclosure[0]["href"])
        print("\n")


# List of RSS feed URLs
rss_u = url

fetch_rss_data(rss_u)
