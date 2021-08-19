#lab 10b
import requests
# Importing request library
url = 'http://www.wikipedia.org’
# Set the target webpage
r = requests.get(url)
# get request
print(r.text)
# This will get the full page of get request

print("Status code:")
# This will show status code:
print("\t *", r.status_code)
# This will get the status code, 200 which also means OK

h = requests.head(url)
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
	'User-Agent' : ‘Mobile’
}
url2 = 'http://httpbin.org/headers'
# Test it on an alternate site
rh = requests.get(url2, headers=headers)
print(rh.text)

print("Hello test edit")
