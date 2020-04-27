import requests
import webbrowser
import httplib2
import webbrowser
import requests

from bs4 import BeautifulSoup

with open('html/index.html') as html_code:
    soup = BeautifulSoup(html_code, 'lxml')

# Prettify the Html Elements
#print(soup.prettify())

# Get the name of the element either its tag or something else
tag = soup.div
span = soup.span
comments = soup.i
print(comments)
#print(type(tag))
print(soup.img.attrs)
print(soup.img)
print(span.string)
print(tag.string)
print(tag.get_attribute_list('class'))
print(tag.get_attribute_list('id'))
print(span.get_attribute_list('class'))


if tag!= '':
      print(tag['class'])
else:
    print('No class found')


# this commands return the complete html elements available inside the tag
#print(soup.head)

# this commands return the name of the parent repsected to the tag
print(soup.body.parent.name)

for item in range(20):
    print(soup.p)
