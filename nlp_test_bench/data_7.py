import wikipedia
import spacy
import time
spacy.require_gpu()
nlp = spacy.load('en')
wikipedia.set_lang("en")
page_7 = wikipedia.page("Apple Inc.")

data_7 = nlp(page_7.content)
print("------------------------------")
print(len(data_7))
print("GPU:: data_7 done")
print("------------------------------")
