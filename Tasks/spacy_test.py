import spacy

nlp = spacy.load('en_core_web_sm')
doc = nlp(u'(12) I am going to the grocery store right now. ')
for token in doc:
    print(token.text, token.dep_)
print("------------------------------------------------")


nlp = spacy.load('en_core_web_sm')
doc = nlp(u'Do you want anything?')
for token in doc:
    print(token.text, token.dep_)
print("------------------------------------------------")




nlp = spacy.load('en_core_web_sm')
doc = nlp(u'I’ve never taken a linguistics course before.')
for token in doc:
    print(token.text, token.dep_)
print("------------------------------------------------")




nlp = spacy.load('en_core_web_sm')
doc = nlp(u'I have never taken a linguistics course before.')
for token in doc:
    print(token.text, token.dep_)
print("------------------------------------------------")



nlp = spacy.load('en_core_web_sm')
doc = nlp(u'(16) I’d like to talk about it at some point but that’ll be a whole new discussion.  ')
for token in doc:
    print(token.text, token.dep_)
print("------------------------------------------------")



