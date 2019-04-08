import wikipedia
import spacy
import time
spacy.require_gpu()
nlp = spacy.load('en')
wikipedia.set_lang("en")

page_4 = wikipedia.page("Deepwater Horizon oil spill")
data_4 = nlp(page_4.content)
print("------------------------------")
print(len(data_4))
print("GPU:: data_4 done")
print("------------------------------")
