###  Web Crawler
scrapy startproject books_crawler  
cd books_crawler  
scrapy genspider books_ books.toscrape.com

To Run:  
scrapy crawl books_


The books_.py is a simple scrapy web crawler
books_2.py is Selenium based scrapy web crawler
(Need to pre install Chrome Webdriver)