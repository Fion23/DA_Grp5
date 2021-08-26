#lab 10b
import requests
# Importing request library
url_link = 'https://www.apple.com/sg/'
# Set the target webpage
R = requests.get(url_link)
# get request
print(R)
# This will get the full page of get request

print("Status code:")
# This will show status code:
print("\t *", R.status_code)
# This will get the status code, 200 which also means OK

h = requests.head(url_link)
# This will just get just the headers
print("Header:")
# This will show Header:
print("**********")
for x in h.headers:
# To print line by line
	print("\t ", x, ":", h.headers[x])
print("**********")

headers = {
# This will modify the headers user-agent
	'User-Agent' : 'Mobile'
}
url_link2 = 'http://www.google.com'
# Test it on an alternate site
RH = requests.get(url_link2, headers=headers)
print(RH.text)


#10c
import scrapy
from scrapy.http.request import Request


class TestSpider(scrapy.Spider):
    name = "test"
    start_urls = ["https://brickset.com/sets/year-2002/"]
    def parse(self, response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'
            yield {
             'Image Link': x.xpath(newsel).extract_first()
            }

    def start_requests(self):
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}

        for url in self.start_urls:
            yield Request(url, headers=headers)


# To recurse to the next page
        Page_selector = '.next a ::attr(href)'
        next_page = response.css(Page_selector).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urjolin(next_page),
                callback =self.parse
            )
	
import unittest

class project(unittest.TestCase):

    def test_EngineType(self):
        print("Testing")

if __name__ == '__main__':
    unittest.main()
