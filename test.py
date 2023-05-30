str = 'father'
print('father' in str)



grammar = nltk.CFG.fromstring("""
    SENTENCE -> Noun_phrase Verb_phrase
    Noun_phrase -> Noun | Determiner Noun
    Verb_phrase -> Verb | Verb Noun_phrase
    Noun -> 'brother' | 'father' |'children' | 'grandparents' | 'niece' | 'uncle' | 'family' | 'basketball' | 'daughter' | 'she' | 'countryside' | 'segun' | 'water' | 'school' | 'those' | 'wife' | 'my' | 'son' | 'mother' | 'second' | parents' | 'siblings'
    Verb -> 'loves' | 'plays' | 'live' | 'celebrate' | 'have' | 'bought' | 'is' | 'fetched' | 'eating' | 'went' | 'unconditionally' | 'are'
    Determiner -> 'the' | 'our' | 'his' | 'they' | 'a' | 'close' | 'him' | 'of' | 'in' | 'to' | 'he' | 'my' | 'her' | 'two' | 'and'
""")
