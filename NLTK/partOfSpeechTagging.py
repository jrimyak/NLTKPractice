#Using NLTK to tag the part of speech of each word of a sentence 

import nltk

print("Enter a sentence:")
sent = str(input())

tokens = nltk.word_tokenize(sent)
print(tokens)

pos_tag = nltk.pos_tag(tokens)
print(pos_tag)
