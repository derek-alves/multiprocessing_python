import threading
import time

number = []

def add_num():
    print("thread 1 sendo executada")
    for i in range(5):
        number.append(i)
        time.sleep(1)
    print("fim da thread")
def show_num(num):
    print("thread 2 sendo executada")
    for i in num:
      print(i)
      time.sleep(1)
    print("fim da thread")

t = threading.Thread(target=add_num(),args=("thread sendo executada"))
t.start()

s = threading.Thread(target=show_num(number),args=("thread sendo executada"))
s.start()
