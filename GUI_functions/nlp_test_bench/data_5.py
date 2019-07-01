import wikipedia
import spacy
import time
spacy.require_gpu()
nlp = spacy.load('en')
wikipedia.set_lang("en")
page_5 = wikipedia.page("World War II")

data_5 = nlp(page_5.content)


print("------------------------------")
print(len(data_5))
print("GPU:: data_5 done")
print("------------------------------")
