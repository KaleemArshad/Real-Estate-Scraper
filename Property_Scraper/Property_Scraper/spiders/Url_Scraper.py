# import scrapy
# from ..items import PropertyScraperItem
#
# class OnTheMarketSpider(scrapy.Spider):
#     name = 'url'
#     page_no = 1
#     URLs_list = []
#     start_urls = [
#         'https://www.onthemarket.com/for-sale/property/london/'
#     ]
#
#     def parse(self, response):
#         items = PropertyScraperItem()
#         urls = response.xpath('//span[@class="title"]/a').css('::attr(href)').extract()
#         OnTheMarketSpider.URLs_list.append(urls)
#         # next_page = response.xpath("//div[@class='page-nav']/ul/li/a[@class='arrow']/@href").get()
#         next_page = 'https://www.onthemarket.com/for-sale/property/london/?page=' + str(OnTheMarketSpider.page_no)
#         if OnTheMarketSpider.page_no < 43:
#             OnTheMarketSpider.page_no += 1
#             yield response.follow(next_page, callback=self.parse)
#
#         for url in OnTheMarketSpider.URLs_list:
#             items['Urls'] = url
#
#         yield items

