from bs4 import BeautifulSoup

import urllib.request

import nltk

from nltk.corpus import stopwords

#Grabbing web content 
response = urllib.request.urlopen("http://php.net/")
html = response.read()

#Stripping the text of the HTML tags
soup = BeautifulSoup(html,"lxml")
text = soup.get_text(strip=True)

#Making an array of all the words pulled from the website
tokens = [t for t in text.split()]
#Making an array to store the words that aren't stop words
clean_tokens = tokens[:]

sr = stopwords.words('english')

#Go through all tokens and remove stop words
for token in tokens:
    if token in stopwords.words('english'):
        clean_tokens.remove(token)

#Making a frequency distribution of all the words
freq = nltk.FreqDist(clean_tokens)

#printing the values then plotting on a line graph
for key,val in freq.items():
    print(str(key) + ':' + str(val))

freq.plot(20,cumulative=False)

