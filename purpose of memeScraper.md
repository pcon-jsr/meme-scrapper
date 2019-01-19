# Purpose of memeScraper:

This Scraper scrapes the title, image and tags for a meme from https://www.memedroid.com.

## Tools used:

Scrapy

## How to run:

Run the memeSpider of memeScraper.
Type this in command line
```
scrapy crawl memebot
```

## Output:

This scraper returns title, image and tags for a meme in a csv file memedroid.csv.
imagexam.py makes use of ocr space api to find texts inside the meme images for classification.

## Future Works to be Performed:
* Scrap memes from more websites.
* Use of machine learning to provide relevant tags to meme without tags.
* Make a suitable GUI for the resulting application.
