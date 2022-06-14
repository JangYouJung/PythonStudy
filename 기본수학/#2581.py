n = int(input())
m = int(input())

sum = 0
min = 10000

for i in range(n,m+1):
    j = 2
    prime = True
    while(j<i):
        if(i%j==0): 
            prime = False
            break
        j+=1
    if(prime and i>1): 
        sum+=i
        if(min>i): min=i

if(sum == 0): print(-1)
else:
    print(sum)
    print(min)