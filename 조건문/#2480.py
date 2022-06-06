a,b,c=input().split()
l = [int(a),int(b),int(c)]
l.sort(reverse=True)
if(l[0]==l[1]==l[2]):
    print(l[0]*1000+10000)
elif(l[0]==l[1]):
    print(l[0]*100+1000)
elif(l[1]==l[2]):
    print(l[1]*100+1000)
else:
    print(l[0]*100)