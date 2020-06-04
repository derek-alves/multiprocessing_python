import threading
import time

number = []

def add_num():
    print("thread 1 sendo executada")
    for i in range(10):
        number.append(i)
        time.sleep(1)
    print("fim da thread")


def show_media(num):
    print("thread 2 sendo executada")
    for i in num:
      aux = 0
      aux = aux + i
      time.sleep(1)

    aux /= 10
    print(aux)
    print("fim da thread")

t = threading.Thread(target=add_num(),args=("thread sendo executada"))
t.start()

s = threading.Thread(target=show_media(number),args=("thread sendo executada"))
s.start()

