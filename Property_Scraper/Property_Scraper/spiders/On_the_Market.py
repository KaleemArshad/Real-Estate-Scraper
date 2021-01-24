import scrapy
from ..items import PropertyScraperItem
import csv

class OnTheMarketSpider(scrapy.Spider):
    name = 'market'
    start_urls = []
    with open("E:/Sajawal's Data/Data/Web Scraping[Scrapy]/Property_Scraper/URLs.csv", 'r')as f:
        data = csv.reader(f)
        for row in data:
            for link in row:
                start_urls.append('https://www.onthemarket.com/' + link)

    def parse(self, response):
        items = PropertyScraperItem()

        title = response.xpath("//div[@class='details-heading']/h1").css("::text").get().strip()
        price = response.xpath("//div[@class='details-heading']/p/span[@class='price-data']").css("::text").get().strip()
        address = response.xpath("//*[@id='property']/div/div[2]/div[3]/div/div[1]/p[2]").css("::text").get()
        Ph_no = response.xpath("//div[@class='content-phone']/a").css("::text").get().strip()
        # IMG_Url = response.xpath("//*[@id='details-results']/div/div[1]/div[1]/div/div[3]/div/picture/img").css("::attr(src)").get()
        agency = response.css("#property-actions .agent-name").css("::text").get().strip()
        description = response.xpath("//*[@id='description-text']/text()").get().strip()

        items['Description'] = description
        items['Agency'] = agency
        # items['IMG_url'] = IMG_Url
        items['Address'] = address
        items['Phone_no'] = Ph_no
        items['Price'] = price
        items['Title'] = title

        yield items
