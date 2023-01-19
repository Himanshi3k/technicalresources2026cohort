t=int(input())
p=True
for i in range(t):
    n=int(input())
    for i in range(2,(n//2)+1):
        if n%i==0:
            p=False
    if p==False:
        print('not prime')
    else:
        print('prime')
