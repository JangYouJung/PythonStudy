n=int(input())
num=map(int,input().split())

count = 0
for i in num:
    j = 2
    prime = True
    while(j<i):
        if(i%j==0): 
            prime = False
            break
        j+=1
    if(prime and i>1): count+=1

print(count)        
        
        