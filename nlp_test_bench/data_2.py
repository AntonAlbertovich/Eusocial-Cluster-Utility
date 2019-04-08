import wikipedia
import spacy
import time
spacy.require_gpu()
nlp = spacy.load('en')
wikipedia.set_lang("en")
page_2 = wikipedia.page("google")
data_2 = nlp(page_2.content)
print("------------------------------")
print(len(data_2))
print("GPU:: data_2 done")
print("------------------------------")
