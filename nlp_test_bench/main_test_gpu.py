from multiprocessing import Process
import wikipedia
import spacy
import time
import sys
import os

spacy.prefer_gpu()
nlp = spacy.load('en_core_web_sm')
wikipedia.set_lang("en")
rando = str(wikipedia.random(pages=0))
page = wikipedia.page(rando)


def func0():
    time_1 = time.time()
    os.system('python3 data_0.py')
    time_1 = time.time() - time_1
    print("GPU:: It took ", time_1, " seconds. data_0 ")
    print("------------------------------")

def func1():
    time_1 = time.time()
    os.system('python3 data_1.py')
    time_1 = time.time() - time_1
    print("GPU:: It took ", time_1, " seconds. data_1 ")
    print("------------------------------")

def func2():
    time_1 = time.time()
    os.system('python3 data_2.py')
    print("------------------------------")
    print("GPU:: It took ", time_1, " seconds. data_2 ")
    print("------------------------------")

def func3():
    time_1 = time.time()
    os.system('python3 data_3.py')
    time_1 = time.time() - time_1
    print("GPU:: It took ", time_1, " seconds. data_3 ")
    print("------------------------------")

def func4():
    time_1 = time.time()
    os.system('python3 data_4.py')
    time_1 = time.time() - time_1
    print("GPU:: It took ", time_1, " seconds. data_4 ")
    print("------------------------------")

def func5():
    time_1 = time.time()
    os.system('python3 data_5.py')
    time_1 = time.time() - time_1
    print("GPU:: It took ", time_1, " seconds. data_5 ")
    print("------------------------------")

def func6():
    time_1 = time.time()
    os.system('python3 data_6.py')
    time_1 = time.time() - time_1
    print("GPU:: It took ", time_1, " seconds. data_6 ")
    print("------------------------------")

def func7():
    time_1 = time.time()
    os.system('python3 data_7.py')
    time_1 = time.time() - time_1
    print("GPU:: It took ", time_1, " seconds. data_7 ")
    print("------------------------------")
if __name__=='__main__':
    p0 = Process(target = func0)
    p0.start()
    
    p1 = Process(target = func1)
    p1.start()
    
    p2 = Process(target = func2)
    p2.start()
    
    p3 = Process(target = func3)
    p3.start()
    p4 = Process(target = func4)
    p4.start()
    p5 = Process(target = func5)
    p5.start()
    p6 = Process(target = func6)
    p6.start()
    #p7 = Process(target = func7)
    #p7.start()


