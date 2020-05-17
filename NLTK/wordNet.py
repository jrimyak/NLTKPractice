from nltk.corpus import wordnet

#WordNet is a database that has groups of synonym and breif definitions

#Definition and example of the word pain
syn = wordnet.synsets("pain")
print(syn[0].definition())
print(syn[0].examples())

#Definition for the word NLP
nlpDef = wordnet.synsets("NLP")
print(nlpDef[0].definition())

#Definition for the word Python
pythonDef = wordnet.synsets("Python")
print(pythonDef[0].definition())

#Getting synonyms of a word 
synonyms = []

for synonym in wordnet.synsets('Computer'):
    for lemma in synonym.lemmas():
        synonyms.append(lemma.name())

print(synonyms)

#Getting antonyms of a word
antonyms = []

for antonym in wordnet.synsets("small"):
    for l in antonym.lemmas():
        if(l.antonyms()):
            antonyms.append(l.antonyms()[0].name())

print(antonyms)