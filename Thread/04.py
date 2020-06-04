from random import randint
import threading
import time

number = []


   
def fibonacci():
     anterior = 0
     proximo = 0
     print('inicio thread')
     while(proximo <= 50):
          print(proximo)
          proximo = proximo + anterior
          anterior = proximo - anterior 

          if(proximo ==0):
             proximo = proximo + 1
      


def thread():
    
    t = threading.Thread(target=fibonacci(),args=("thread sendo executada"))

    s = threading.Thread(target=fibonacci(),args=("thread sendo executada"))
    t,s.start()


thread()
