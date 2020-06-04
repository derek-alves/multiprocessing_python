import os

def parent_child(): 
    r, w = os.pipe()
    n = os.fork() 
    if n > 0: 
        print("Parent process and id is : ", os.getpid()) 
        os.close(w)
        r = os.fdopen(r) 
        read = r.read() 
        print( "Parent reads =", read)
    else: 
        print("Child process and id is : ", os.getpid()) 
        a = fibonacci_loop(5)
        os.close(r) 
        w = os.fdopen(w, 'w') 
        print ("Child writing") 
        w.write(a) 
        w.close()   
        

def fibonacci_loop(num):
    if num == 0:
         return 0
    elif num == 1 or num == 2:
        return 1
    elif num > 2:
        a = 1 
        b = 1 
        for _ in range(3, num + 1):
            c = a + b
            a, b = b, c

        return c