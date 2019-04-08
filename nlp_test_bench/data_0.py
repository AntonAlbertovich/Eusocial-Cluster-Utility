import wikipedia
import spacy
import time
spacy.require_gpu()
nlp = spacy.load('en')
wikipedia.set_lang("en")
page_0 = wikipedia.page("IBM")
data_0 = nlp(page_0.content)
print("------------------------------")
print(len(data_0))
print("GPU:: data_0 done")
print("------------------------------")
