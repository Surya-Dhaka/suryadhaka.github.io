import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
link = soup.select('.titleline > a')
subtext = soup.select('.subtext')

def sort_stories_by_votes(hnlist):
  return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

def create_custom_hackernews(link, subtext):
	hackernews = []
	for inx, item in enumerate(link):
		title = item.getText()
		href = item.get('href', None)
		vote = subtext[inx].select('.score')
		if len(vote):
			points = int(vote[0].getText().replace(' points', ''))
			if points > 99:
				hackernews.append({'title': title, 'link': href, 'votes': points})
	return sort_stories_by_votes(hackernews)

pprint.pprint(create_custom_hackernews(link, subtext))