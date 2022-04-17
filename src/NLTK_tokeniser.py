import nltk
#nltk.download('punkt')

from nltk.tokenize import word_tokenize, sent_tokenize

file = open("/Users/rajat/Documents/Uni/SER502/SER502-Spring2022-Team7/src/test.txt", "r")
text = file.read()
specials = '+-*/%='

token = word_tokenize(text)
print(token)