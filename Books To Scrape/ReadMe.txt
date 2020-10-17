###  Web Crawler
scrapy startproject books_crawler  
cd books_crawler  
scrapy genspider books_ books.toscrape.com

To Run:  
scrapy crawl books_


The books_.py is a simple scrapy web crawler that fetches URL's

books_2.py is Selenium based scrapy web crawler
(Need to pre install Chrome Webdriver)

books_3.py is a complete webscraper using scrapy which extracts data 
as well as goes through all URLs to fetch it.
To store data in csv 
Run: scrapy crawl books_3 -o books.csv 