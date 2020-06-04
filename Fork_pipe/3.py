import os
 
lista = []
def parent_child(): 
    r, w = os.pipe() 
    n = os.fork() 
    if n > 0: 
        print("Parent process and id is : ", os.getpid())
        os.close(w)
        r = os.fdopen(r) 
        print ("Parent reading") 
        read = r.read() 
        print( "Parent reads =", read)
    else: 
        pid, status = os.wait()
        print("Child process and id is {} and status {}: ".format(pid,status)) 
        valor = 8;  
        fatorial = 1  
        while (valor > 1):  
            child_writes = fatorial * valor  
            valor = valor - 1
            os.close(r) 
            w = os.fdopen(w, 'w') 
            print ("Child writing") 
            w.write(child_writes) 
            w.close()   
        
 
 
exitstat = 0
 
 
# Function that is executed after os.fork() that runs in a new process
def child():
    global exitstat
    exitstat += 1
    print('Hello from child', os.getpid(), exitstat)
     
    # End this process using os._exit() and pass a status code back to the shell
    os._exit(exitstat)
 
 
# This is the parent process code
def parent():
    while True:
        # Fork this program into a child process
        newpid = os.fork()
         
        # newpid is 0 if we are in the child process
        if newpid == 0:
            # Call child()
            child()
             
        # otherwise, we are still in the parent process
        else:
            # os.wait() returns the pid and status and status code
            # On unix systems, status code is stored in status and has to
            # be bit-shifted
            pid, status = os.wait()
            print('Parent got', pid, status, (status >> 8))
            if input() == 'q':
                break
 
 
if __name__ == '__main__':
    parent()