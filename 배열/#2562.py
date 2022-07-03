max=0
order=0

for i in range(1,10):
    n=int(input())
    if(n>max):
        max=n
        order=i
        
print(max)
print(order)