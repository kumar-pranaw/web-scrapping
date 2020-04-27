import requests
import re
import webbrowser
from bs4 import BeautifulSoup

url = 'https://mashable.com/2014/08/28/static-website-generators'

resp = requests.get(url)

parsedHtml = BeautifulSoup(resp.text, "lxml")

#print(parsedHtml.prettify())
# this will print all link start from http [it can be http:// or https://]
# this will provide only absolute links for the external links
# for allHrefs in parsedHtml.findAll('a', attrs = {'href': re.compile("^http")}):
#     # print(allDivs.text)
#     print(allHrefs["href"])

# print("\n \n \n \n")
# print("Relaitve Links \n \n")
# to find all the absolute and all the relative links we can use something like this
# for links in parsedHtml.findAll('a', href= True):
#     # print(allDivs.text)
#     print(links["href"])
    
# Prefixing the link which is relative url with the base url
for links in parsedHtml.findAll('a', href= True):
    if not links['href'].startswith('http'):
        links = url + links['href'].strip('/')
    else:
        links = links['href']
        
    print(links)
    #webbrowser.open(links)