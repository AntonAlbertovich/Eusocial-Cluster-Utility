import wikipedia
import spacy
import time
spacy.require_gpu()
nlp = spacy.load('en')
wikipedia.set_lang("en")
page_3 = wikipedia.page("Microsoft")
data_3 = nlp(page_3.content)
print("------------------------------")
print(len(data_3))
print("GPU:: data_3 done")
print("------------------------------")
