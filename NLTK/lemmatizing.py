#Lemmatizing a word is like stemming however the result is a real word
#Lemmatizing is a slower process than stemming 
#Lemmatizing is more accurate 
#See the difference between Stemming and Lemmatizing

from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

print(stemmer.stem('increases'))
print(lemmatizer.lemmatize('increases'))

#For lemmatizing you may end up with a synonym
#For a word like playing, you may need ot specify the part of speech since the default part of speech is a noun
#To get a verb you would need to specify it
#verb
print(lemmatizer.lemmatize('playing', pos="v"))
#noun
print(lemmatizer.lemmatize('playing', pos="n"))
#adjective 
print(lemmatizer.lemmatize('playing', pos="a"))
#adverb
print(lemmatizer.lemmatize('playing', pos="r"))

#See the difference between stemming and lemmatization
print('Stemming')
print('----------------------')
print(stemmer.stem('stones'))
print(stemmer.stem('speaking'))
print(stemmer.stem('bedroom'))
print(stemmer.stem('jokes'))
print(stemmer.stem('lisa'))
print(stemmer.stem('purple'))
print('----------------------')
print("Lemmatizing")
print('----------------------')
print(lemmatizer.lemmatize('stones'))
print(lemmatizer.lemmatize('speaking'))
print(lemmatizer.lemmatize('bedroom'))
print(lemmatizer.lemmatize('jokes'))
print(lemmatizer.lemmatize('lisa'))
print(lemmatizer.lemmatize('purple'))