import wikipedia
import spacy
import time
spacy.require_gpu()
nlp = spacy.load('en')
wikipedia.set_lang("en")
page_6 = wikipedia.page("Artificial intelligence")

data_6 = nlp(page_6.content)
print("------------------------------")
print(len(data_6))
print("GPU:: data_6 done")
print("------------------------------")
