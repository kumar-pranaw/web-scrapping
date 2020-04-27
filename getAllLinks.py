import requests
import re
import webbrowser
from bs4 import BeautifulSoup

url = 'https://mashable.com/2014/08/28/static-website-generators'

resp = requests.get(url)

parsedHtml = BeautifulSoup(resp.text, "lxml")

#print(parsedHtml.prettify())
# this will print all link start from http [it can be http:// or https://]
for allHrefs in parsedHtml.findAll('a', attrs = {'href': re.compile("^http")}):
    # print(allDivs.text)
    print(allHrefs["href"])