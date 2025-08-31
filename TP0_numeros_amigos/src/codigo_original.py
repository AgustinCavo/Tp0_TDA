import time
def amigos(MAX):
    
    t1=time.time()
    for i in range(MAX):
        s=0
        for j in range (1,i-1+1):
            if i%j==0:
                s+=j
        s2=0
        for k in range (1,s-1):
            if s%k==0:
                s2+=k
        if i==s2:
            print(i,s)
   
    t2=time.time()    
    print(t2-t1)

amigos(150000)