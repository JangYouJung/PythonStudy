A= int(input())
B= int(input())
C= int(input())
mul=str(A*B*C)

for i in range(0,10):
    num=0
    for j in mul:
        if(i==int(j)):
            num+=1
    
    print(num)

