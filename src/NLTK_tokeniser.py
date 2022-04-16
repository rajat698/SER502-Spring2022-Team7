import nltk
#nltk.download('punkt')

from nltk.tokenize import word_tokenize, sent_tokenize

file = open("src/test.txt", "r")
text = file.read()
specials = '+-*/%='

token = word_tokenize(text)
print(token)