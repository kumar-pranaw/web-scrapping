import requests
import webbrowser
import httplib2
import webbrowser
import requests

from bs4 import BeautifulSoup


resp= requests.get("http://www.google.com")
#print(resp.text)

soup = BeautifulSoup(resp.text, "html5lib")
print(soup.prettify())