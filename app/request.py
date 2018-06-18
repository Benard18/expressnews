import urllib.request,json
from .models import News,Article

#Getting api key
api_key = None
base_url = None
article_base_url = None
headlines_url = None

#Getting the news base url
def configure_request(app):
	global api_key,base_url,article_base_url,headlines_url
	api_key = app.config["NEWS_API_KEY"]
	base_url = app.config["SEARCH_API_BASE_URL"]
	article_base_url = app.config["NEWS_ARTICLE_API_BASE_URL"]
	headlines_url = app.config["HEADLINES_API_BASE_URL"]

def process_results(news_list):
	'''
	Function that processes that news result and transform them to a list of objects
	
	Args:
		news_list: Alist of dictionaries  that contain news details

	Returns :
		news_results = A list of news objects
	'''
	News_results=[]
	for news_item in news_list:
		id = news_item.get('id')
		name = news_item.get('name')
		description = news_item.get('description')
		url = news_item.get('url')
		category = news_item.get('category')

		news_object = News(id,name,description,url,category)
		News_results.append(news_object)

	return News_results

def get_news(category):
	'''
	Function that gets json response to our url request
	'''
	get_news_url =base_url.format(category,api_key)
	print(get_news_url)
	with urllib.request.urlopen(get_news_url) as url:
		get_news_data = url.read()
		get_news_response = json.loads(get_news_data)

		news_results = get_news_response
	
		if get_news_response['sources']:
			news_results_list = get_news_response['sources']
			news_results = process_results(news_results_list)



	return news_results		

def process_articles(articles_list):
    article_results = []
    for item in articles_list:
        author = item.get('author')
        title = item.get('title')
        description = item.get('description')
        url = item.get('url')
        image_url = item.get('urlToImage')
        publish_time = item.get('publishedAt')

        articles_object = Article(author, title, description, url, image_url, publish_time)
        article_results.append(articles_object)

    return article_results
            
def get_articles(id):
    '''
    function to get json response from url
    '''
  
    get_articles_details_url = article_base_url.format(id, api_key)
    print(get_articles_details_url)
    with urllib.request.urlopen(get_articles_details_url) as url:
        articles_details_data = url.read()
        articles_details_response = json.loads(articles_details_data)

        articles_results = None
    
        if articles_details_response['articles']:
            article_results_list = articles_details_response['articles']
            articles_results = process_articles(article_results_list)
    
    return articles_results

def process_headlines(headlines_list):
    headline_results = []
    for item in headlines_list:
        author = item.get('author')
        title = item.get('title')
        description = item.get('description')
        url = item.get('url')
        image_url = item.get('urlToImage')
        publish_time = item.get('publishedAt')

        headlines_object = Article(author, title, description, url, image_url, publish_time)
        headline_results.append(headlines_object)

    return headline_results
            
def get_headlines(category):
    '''
    function to get json response from url
    '''
    
    get_headlines_url = headlines_url.format(category, api_key)

    with urllib.request.urlopen(get_headlines_url) as url:
        headlines_details_data = url.read()
        headlines_details_response = json.loads(headlines_details_data)

        headlines_results = None
        print(headlines_details_data)
        if headlines_details_response['articles']:
            headlines_results_list = headlines_details_response['articles']
            headlines_results = process_articles(headlines_results_list)
    
    return headlines_results

