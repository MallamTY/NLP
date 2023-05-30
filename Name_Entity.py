import nltk
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
lemmitizer = WordNetLemmatizer()
str_to_lemmatize = "It's a dangerous business, Frodo, going out your door"
tokenized_words = word_tokenize(str_to_lemmatize)
pos_tagged = nltk.pos_tag(tokenized_words)
tree = nltk.ne_chunk(pos_tagged)
tree.draw()