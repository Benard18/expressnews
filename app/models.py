class News:
	'''
	News class to define News Objects
	'''
	def __init__(self, id, name, description, url, category):
		self.id = id
		self.name = name
		self.description = description
		self.url = url
		self.category = category

class Article:
    '''
    class to define article objects
    '''
    def __init__(self, author, title, description, url, image_url, publish_time):
        self.author = author
        self.title = title
        self.description = description
        self.url = url 
        self.image_url = image_url
        self.publish_time = publish_time