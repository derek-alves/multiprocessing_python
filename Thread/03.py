from random import randint
import threading
import time

number = []

def add_num():
    for i in range(50):
        number.append(randint(0,50))
   
def show(num):
    print("thread 1 sendo executada")
    for i in range(25):
      print(number[i])
    print("fim da thread")


def show2(num):
    print("thread 2 sendo executada")
    for i in range(len(number)-1,24,-1):
      print(number[i])
    print("fim da thread")

add_num()

t = threading.Thread(target=show(number),args=("thread sendo executada"))
t.start()

s = threading.Thread(target=show2(number),args=("thread sendo executada"))
s.start()
