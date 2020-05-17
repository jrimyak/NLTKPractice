from nltk.tokenize import sent_tokenize

from nltk.tokenize import word_tokenize

mytext = "Hello Mr. Adam, how are you? I hope everything is going well. Today is a good day, see you dude."
mytextFrench = "Bonjour M. Adam, comment allez-vous? J'espère que tout va bien. Aujourd'hui est un bon jour."

#Utilizing sentence tokenizer from NLTK to print each sentence of a string
print(sent_tokenize(mytext))

#Utilizing word tokenizer from NLTK to print each word in a string
print(word_tokenize(mytext))

#Utilizing the sentnece tokenizer in a another language other than english
print(sent_tokenize(mytextFrench, "French"))