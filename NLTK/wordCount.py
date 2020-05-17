from bs4 import BeautifulSoup

import urllib.request

import nltk


#Grabbing web content data
response = urllib.request.urlopen('http://php.net/')
html = response.read()

#Use BeautifulSoup to clean text from the webpage
soup = BeautifulSoup(html,"lxml")
text = soup.get_text(strip=True)

#Convert into tokens
tokens = [t for t in text.split()]

#Use NLTK to count words by calculating the frequency distribution 
freq = nltk.FreqDist(tokens)

for key,val in freq.items():
    print(str(key) + ':' + str(val))

#plot a graph of the freequency of text
freq.plot(20, cumulative=False)