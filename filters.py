import re
from bs4 import  BeautifulSoup

with open('html/index.html') as html_code:
    soup = BeautifulSoup(html_code, 'lxml')

#print(soup.prettify())

divs = soup.findAll('img')
imageFilter = soup.findAll(src = 'images/resources/challenge-covid.png')
print(imageFilter)
print(soup.find('title'))
print(soup.findAll('span'))

#print(divs)

# Get the list of all which starts with img tag similarly we can achieve
# finding all the list of tags  by adding ^ sign before the letter or tag name
for divs in soup.findAll(re.compile("^img")):
    print(divs)

# to find or parse using the certain attribute by certain class

print(soup.find('div', attrs = {'class': re.compile('^vid_')}))

# using regular expression to filter the elements using attribute
# finding all divs having class starts with ^vid_

for allDivs in soup.findAll('div', attrs = {'class': re.compile('^vid_')}):
    print(allDivs.text)

# using regular expression to filter the elements using attribute
# finding all divs contains c lass vid

for allDivs in soup.findAll('div', attrs = {'class': re.compile('vid')}):
    # print(allDivs.text)
    print(allDivs.a)

#using regular expression to filter the elements using tag
for allDivs in soup.findAll(re.compile("it")):
    # print(allDivs.text)
    print(allDivs)
    # this will only return the name of the tag
    print(allDivs.name)
print("#########################################################################################")   
print("#########################################################################################")
print("#########################################################################################")

# finding all elements having id     
for allDivs in soup.findAll(id= re.compile("vvideo_tabz")):
    print(allDivs.text)
    print(allDivs.name)
    print(allDivs.text)

# find all html elements which have their href pointing to some particular text
for allDivs in soup.findAll(href= re.compile("single")):
    print(allDivs.text)
    print(allDivs.name)
    print(allDivs.text)