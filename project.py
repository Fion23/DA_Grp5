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

class TestSpider(scrapy.Spider):
    name = "test"
    start_urls = ["https://www.bricksworld.com/"]
    def parse(self, response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'
            yield {
             'Image Link': x.xpath(newsel).extract_first()
            }

# To recurse to the next page
        Page_selector = '.next a ::attr(href)'
        next_page = response.css(Page_selector).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urjolin(next_page),
                callback =self.parse
            )

