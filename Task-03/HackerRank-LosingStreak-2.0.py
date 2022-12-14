a=2
L= list(map(int,input().strip().split()))[:a]
n=L[0]
m=L[1]
sol1=0
sol2=0
d=m/n
q=m/n
while m%n==0 and d%2==0:
    d=d/2
    sol1 += 1
while m%n==0 and d%3==0:
    d=d/3
    sol2 +=  1

if n > m:
    print("-1")
elif m==n:
    print("0")
elif m>n and d==1 :
    print(int(sol1+sol2))
else:
    print(-1)
