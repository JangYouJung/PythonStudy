
n = int(input())

for n in range(n):
    line = input()
    vps = True
    stack = []
    for k in line:
        if(k == '('):
            stack.append('(')
        else:
            if not stack:
                vps = False
                break
            elif(stack.pop(-1)!='('):
                vps=False
                break
    
    if stack: vps = False
    
    if(vps): print("YES")
    else: print("NO")
