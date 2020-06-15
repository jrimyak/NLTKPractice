#Using NLTK to tag the part of speech of each word of a sentence 

import nltk
#Asks the user to enter a sentence
print("Enter a sentence:")
sent = str(input())
#Tokenizes the words 
tokens = nltk.word_tokenize(sent)
print(tokens)
#Tags each words part of speech
pos_tag = nltk.pos_tag(tokens)
print(pos_tag)
