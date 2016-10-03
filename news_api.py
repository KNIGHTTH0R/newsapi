import requests
import json
from json_handler import Source

APIKEYFILE = 'newsapikey'


def get_key():
	key = ''
	with open(APIKEYFILE, 'r') as f:
		key = f.read()
	return key

def get_sources(category=None, language=None, country=None):
	uri = 'https://newsapi.org/v1/sources'
	params = '?'
	if category is not None:
		params += 'category=' + category + '&'
	if language is not None:
		params += 'language=' + language + '&'
	if country is not None:
		params += 'country=' + country
	r = requests.get(uri+params)
	return r

def get_articles(source, sortBy=None):
	key = get_key()
	uri = 'https://newsapi.org/v1/articles'
	params = '?source=' + source + '&apiKey=' + key
	if sortBy is not None:
		params += '&sortBy=' + sortBy
	r = requests.get(uri+params)
	return r

def make_sources(json_data):
	data = json.loads(json.dumps(json_data))
	if 'sources' in data:
		sources = []
		for source in data['sources']:
			sources.append(Source(source))
		return sources