class Source(object):

	def __init__(self, json_source):
		self.category = json_source['category']
		self.description = json_source['description']
		self.language = json_source['language']
		self.sortBysAvailable = json_source['sortBysAvailable']
		self.url = json_source['url']
		self.country = json_source['country']
		self.urlsToLogos = json_source['urlsToLogos']
		self.id = json_source['id']
		self.name = json_source['name']