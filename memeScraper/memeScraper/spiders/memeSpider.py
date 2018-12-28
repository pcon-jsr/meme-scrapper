# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 15:10:15 2018

@author: ADARSH ANURAG
"""
from scrapy import Spider
from scrapy.selector import Selector
from memeScraper.items import Meme

class MemeSpider(Spider):
    name ="memebot"
    allowed_domain = ["https://www.memedroid.com"]
    start_urls = ["https://www.memedroid.com/memes/latest/"]
    
    def parse(self,response):
        Title=[]
        Image=[]
        Tags=[]
        container = response.xpath("//div[@class='gallery-memes-container']")
        articles = container.xpath(".//article")
        for article in articles:
            title = article.xpath(".//div[@class='item-aux-container']/header/h1/a/text()").extract()
            Title.append(title[0])
            image_link = article.xpath(".//div[@class='item-aux-container']/a[@class='dyn-link']/img/@src").extract()
            Image.append(image_link[0])
            tag = article.xpath(".//div[@class='tags-container']/a/text()").extract()
            Tags.append(tag)
            print('\n')
        Item = Meme()
        for item in zip(Title,Image, Tags):
            Item['title'] = item[0]
            Item['image'] = item[1]
            Item['tags'] = item[2]
            yield Item
