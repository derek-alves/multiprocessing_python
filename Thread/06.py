
import threading
import time

valor = 100
valor1 = 5
   
def soma(num, num1):
    result = num + num1
    print("soma:", result)

def sub(num, num1):
    result = num - num1
    print("subtração:", result)    

def div(num, num1):
    result = num / num1
    print("divisão:", result)


 
s = threading.Thread(target=soma(valor,valor1),args=("thread sendo executada"))
ss= threading.Thread(target=sub(valor,valor1),args=("thread sendo executada"))
d = threading.Thread(target=div(valor,valor1),args=("thread sendo executada"))
s,ss,d.start()

