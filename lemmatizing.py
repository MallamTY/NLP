import nltk
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
lemmitizer = WordNetLemmatizer()
str_to_lemmatize = "The friends of DeSoto love scarves."
tokenized_words = word_tokenize(str_to_lemmatize)
lemmitizer_str = [lemmitizer.lemmatize(word) for word in tokenized_words]
#print(lemmitizer_str)
