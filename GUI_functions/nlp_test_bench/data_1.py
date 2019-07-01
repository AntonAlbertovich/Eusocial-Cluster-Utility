import wikipedia
import spacy
import time
spacy.require_gpu()
nlp = spacy.load('en')
wikipedia.set_lang("en")
page_1 = wikipedia.page("Algorithm")

data_1 = nlp(page_1.content)
print("------------------------------")
print(len(data_1)) 
print("GPU:: data_1 done")
print("------------------------------")
