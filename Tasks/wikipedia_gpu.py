import wikipedia
import spacy
import time
spacy.require_gpu()
nlp = spacy.load('en_core_web_sm')
wikipedia.set_lang("en")
rando = str(wikipedia.random(pages=0))
page = wikipedia.page(rando)

page_0 = wikipedia.page("google")

page_1 = wikipedia.page("Apple Inc.")

page_2 = wikipedia.page("IBM")

page_3 = wikipedia.page("Microsoft")

page_4 = wikipedia.page("Deepwater Horizon oil spill")

page_5 = wikipedia.page("Artificial intelligence")

page_6 = wikipedia.page("World War II")

page_7 = wikipedia.page("Algorithm")

time_master = time.time()

time_0 = time.time()
data_0 = nlp(page_0.content)
time_0 = time.time() - time_0

time_1 = time.time()
data_1 = nlp(page_1.content)
time_1 = time.time() - time_1

time_2 = time.time()
data_2 = nlp(page_2.content)
time_2 = time.time() - time_2

time_3 = time.time()
data_3 = nlp(page_3.content)
time_3 = time.time() - time_3

time_4 = time.time()
data_4 = nlp(page_4.content)
time_4 = time.time() - time_4

time_5 = time.time()
data_5 = nlp(page_5.content)
time_5 = time.time() - time_5

time_6 = time.time()
data_6 = nlp(page_6.content)
time_6 = time.time() - time_6

time_7 = time.time()
data_7 = nlp(page_7.content)
time_7 = time.time() - time_7

time_master = time.time() - time_master

#print("------------------------------")
#for token in doc:
# print(token.text, token.pos_, token.dep_)
#print(page.content)
print("------------------------------")
print("GPU:: It took ", time_0, " seconds. data_0 ")
print("------------------------------")
print("GPU:: It took ", time_1, " seconds. data_1 ")
print("------------------------------")
print("GPU:: It took ", time_2, " seconds. data_2 ")
print("------------------------------")
print("GPU:: It took ", time_3, " seconds. data_3 ")
print("------------------------------")
print("GPU:: It took ", time_4, " seconds. data_4 ")
print("------------------------------")
print("GPU:: It took ", time_5, " seconds. data_5 ")
print("------------------------------")
print("GPU:: It took ", time_6, " seconds. data_6 ")
print("------------------------------")
print("GPU:: It took ", time_7, " seconds. data_7 ")
print("------------------------------")
print("GPU:: It took ", time_master, " seconds. For all cases. ")
print("------------------------------")
