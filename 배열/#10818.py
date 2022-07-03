N=int(input())
numbers=list(map(int,input().split()))

min=numbers[0]
max=numbers[0]

for i in range(N):
    if(min>numbers[i]):
        min=numbers[i]
    elif(max<numbers[i]):
        max=numbers[i]
        
print(str(min)+' '+str(max))