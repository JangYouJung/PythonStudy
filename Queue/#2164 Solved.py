from collections import deque

N = int(input())
deque= deque([i for i in range(1,N+1)])

while(len(deque)>1):
    deque.popleft()
    a=deque.popleft()
    deque.append(a)
    
print(deque[0])