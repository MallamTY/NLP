import nltk

grammar = nltk.CFG.fromstring("""
    SENTENCE -> Noun_phrase Verb_phrase
    Noun_phrase -> Noun | Determiner Noun
    Verb_phrase -> Verb | Verb Noun_phrase
    Noun -> 'brother' | 'father' | 'children' | 'grandparents' | 'niece' | 'uncle' | 'family' | 'basketball' | 'daughter' | 'she' | 'countryside' | 'segun' | 'water'| 'school'| 'those' | 'wife' | 'my'  | 'son' | 'mother' | 'second' | 'parents' | 'siblings' | 'he' | 'funmi' | 'emmanuel' | 'ade' | 'classmate'
    Verb -> 'loves' | 'plays' | 'live' | 'celebrate' | 'have' | 'bought' | 'is' | 'fetched' | 'eating' | 'went' | 'unconditionally' | 'are' | 'has' | 'coming'
    Determiner -> 'my' | 'the' | 'our' | 'his' | 'they' | 'a' | 'close' | 'him' | 'of' | 'in' | 'to' | 'her' | 'two' | 'and'
""")

sentence_parser = nltk.ChartParser(grammar)

sentences = [
    "Ade has a son",
    "Mother loves her children",
    "Those two are father and son",
    "Emmanuel wife is coming",
    "Segun parents are coming",
    "His daughter is my classmate"
]

for sentence in sentences:
    words = nltk.word_tokenize(sentence.lower())
    trees = list(sentence_parser.parse(words))
    parsed = False
    for tree in trees:
        tree.pretty_print()
        parsed = True
    if parsed: 
        print(f"\nThe sentence: '{sentence}' is grammatically correct \n")

    else:
        print(f"\nThe sentence: '{sentence}' is grammatically incorrect")


