import nltk
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
lemmitizer = WordNetLemmatizer()
str_to_lemmatize = "Simbi is the first daughter of the family come first in countryside"
tokenized_words = word_tokenize(str_to_lemmatize)
print(nltk.help.upenn_tagset())
pos_tagged = nltk.pos_tag(tokenized_words)
grammar = """
Chunk: {<.*>+}
}<JJ>{"""
chunk_parser = nltk.RegexpParser(grammar)
tree = chunk_parser.parse(pos_tagged)
print(pos_tagged)
# print(tree)
# print(tree.draw())
#print(lemmitizer_str)

[('Simbi', 'NNP'), ('is', 'VBZ'), ('the', 'DT'), ('first', 'JJ'), ('daughter', 'NN'), ('of', 'IN'), ('the', 'DT'), ('family', 'NN'), ('come', 'VB')]