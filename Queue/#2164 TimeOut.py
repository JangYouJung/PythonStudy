n = int(input())
cards = []

for i in range(1,n+1):
    cards.append(i)
    
while(1):       
    cards.pop(0)
    if(len(cards) == 1):
        print(cards[0])
        break
    
    cards.append(cards[0])
    cards.pop(0)
    