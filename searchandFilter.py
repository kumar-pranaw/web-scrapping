# Searching and Filtering Using Custom Functions
import re
from bs4 import  BeautifulSoup

with open('html/index.html') as html_code:
    soup = BeautifulSoup(html_code, 'lxml')

#Finds all the html elements for anchor and images tag
print(soup.findAll(['a', 'img']))

for tags in soup.findAll(True):
    print(tags.name)

def has_src_but_no_href(tag):
    return tag.has_attr('src') and not tag.has_attr('href')

print(soup.findAll(has_src_but_no_href))

def has_no_(href):
    return href and not re.compile("single_video").search(href)

print(soup.findAll(href = has_no_))