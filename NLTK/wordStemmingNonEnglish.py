#Using the SnowballStemmer works for stemming 14 different languages

from nltk.stem import SnowballStemmer
#Prints out all the languages the Snowball Stemmer can stem with 
print(SnowballStemmer.languages)

#Asking the user to enter a french word
print("Enter a french word")
french_stemmer = SnowballStemmer('french')

#stem the french word
word = str(input())
print(french_stemmer.stem(word))