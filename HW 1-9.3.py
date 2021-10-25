from pprint import pprint
import requests


class Reddit:

    def get_popular_videos(self):
        url = "https://www.reddit.com/r/gifs/top.json?t=day"
        response = requests.get(url, headers={'User-agent': 'netology'})
        pprint(response)
        return response.json()

if __name__ == '__main__':
    reddit = Reddit()
    pprint(reddit.get_popular_videos())
