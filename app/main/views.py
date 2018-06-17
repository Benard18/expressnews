from flask import render_template,url_for,request,redirect
from . import main
from ..request import get_news,get_articles,get_headlines

#Views
@main.route('/')
def index():
	'''
	View root page function that returns the index page and its data
	'''
	# Getting popular news
	general_news = get_headlines('general')
	title = 'Home Page - Get The latest News Online Across The World'
	return render_template('index.html',title = title,general=general_news)

@main.route('/general')
def general():

	general_news = get_news('general')
	title = 'Home Page - Get The latest News Online Across The World'
	return render_template('general.html',general=general_news)

@main.route('/business')
def business():

	business_news = get_news('business')
	title = 'Home Page - Get The latest News Online Across The World'
	return render_template('business.html',business=business_news)

@main.route('/sports')
def sports():

	sports_news = get_news('sports')
	title = 'Home Page - Get The latest News Online Across The World'
	return render_template('sports.html',sports=sports_news)

@main.route('/science')
def science():

	science_news = get_news('science')
	title = 'Home Page - Get The latest News Online Across The World'
	return render_template('science.html',science=science_news)

@main.route('/entertainment')
def entertainment():

	entertainment_news = get_news('entertainment')
	title = 'Home Page - Get The latest News Online Across The World'
	return render_template('entertainment.html',entertainment=entertainment_news)

@main.route('/technology')
def technology():

	technology_news = get_news('technology')
	title = 'Home Page - Get The latest News Online Across The World'
	return render_template('technology.html',technology=technology_news)

@main.route('/health')
def health():

	health_news = get_news('health')
	title = 'Home Page - Get The latest News Online Across The World'
	return render_template('health.html',health=health_news)
@main.route('/templates/article/<id>')
def article(id):
    '''
    returns articles 
    '''
    article_news = get_articles(id)
    
    title = f'{id}'

    return render_template('article.html', title = title, article = article_news)
