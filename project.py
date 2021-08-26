# Use the Request library
import requests
# Set the target webpage
link1 = 'https://brickset.com/sets/year-2002'
req = requests.get(link1)
# This will get the full page
print(req.text)
# This will get the status code
print("Status code:")
print("\t *", req.status_code)
# This will just get just the headers
h = requests.head(link1)
print("Header:")
print("**********")
# To print line by line
for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("**********")
# This will modify the headers user-agent
headers = {
    'User-Agent' : 'Mobile'
}
# Test it on an another site
link2 = 'http://httpbin.org/headers'
reqh = requests.get(link2, headers=headers)
print(reqh.text)



import scrapy
from scrapy.http.request import Request


class Grp5Spider(scrapy.Spider):
    name = "grp5"
    start_urls = ["https://brickset.com/sets/year-2002/"]
    def parse(self, response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'
            yield {
             'Image Link': x.xpath(newsel).extract_first()
            }

    def start_requests(self):
        headers = {'User-Agent': 'Mobile'}

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
