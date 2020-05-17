#Word stemming means removing affixes form words and return the root word
#"Working" becomes "work"
#Use the NLTK implemention of the Porter stemming algorithm
#There are different algorithms for stemming words such as the Lancaster algorithms where some words will be different
from nltk.stem import PorterStemmer

#Create a new stemmer
stemmer = PorterStemmer()

#Take input from the user then stem the word using the stemmer
string = str(input())
print(stemmer.stem(string))