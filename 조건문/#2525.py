hour,minute= map(int,input().split())
minute+=int(input())

if(minute>=60):
    hour+=(minute//60)
    minute%=60
    
if(hour>23):
    hour%=24
    
print(hour,minute)