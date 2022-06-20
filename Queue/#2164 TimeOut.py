n = int(input())
cards = []

for i in range(1,n+1):
    cards.append(i)
    
while(1):   
    if(len(cards) == 1):
        print(cards[0])
        break
    
    cards.pop(0)
    cards.append(cards[0])
    cards.pop(0)
    