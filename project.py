
import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

word_quote = "It's a dangerous business, Frodo, going out your door."
word_in_quote = word_tokenize(word_quote)
str = nltk.pos_tag(word_in_quote)

grammar = "NP: {<DT>?<JJ>*<NN>}"

# stop_words = set(stopwords.words("english"))
# filtered_list = []

# for word in word_in_quote:
#     if word.casefold() not in stop_words:
#         filtered_list.append(word)

# print(filtered_list)

