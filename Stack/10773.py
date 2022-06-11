stack = []
k = int(input())

for i in range(k):
    n = int(input())
    if(n == 0):
        stack.pop()
    else:
        stack.append(n)

sum = 0
for i in stack:
    sum += i
    
print(sum)