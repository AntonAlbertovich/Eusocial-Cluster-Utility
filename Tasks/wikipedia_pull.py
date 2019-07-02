import wikipedia
import spacy
import time

spacy.prefer_gpu()
nlp = spacy.load('en_core_web_sm')
wikipedia.set_lang("en")
rando = str(wikipedia.random(pages=0))
page = wikipedia.page(rando)

page_0 = wikipedia.page("google")

time_0 = time.time()
doc_0 = nlp(page_0.content)
time_0 = time.time() - time_0
#print("------------------------------")
#for token in doc:
# print(token.text, token.pos_, token.dep_)
#print(page.content)
print("------------------------------")
print("GPU:: It took ", time_0, " seconds.")
print("------------------------------")
