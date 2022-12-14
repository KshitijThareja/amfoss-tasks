t=int(input())
n=int(1)
m=[]
manareq=int(0)
if t<=0:
    t=int(input())

for n in range(0,t):
    N=int(input())
    P= list(map(int,input().strip().split()))[:N]
    P.sort()
    lenP=len(P)
    if lenP<N:
        L=N-lenP
        for l in range (1,L):
            P.append(0)
    P.sort()
    ele=int(0)
    for ele in range (0,lenP-1):
        ele1=P[ele]
        ele2=P[ele+1]
        if ele1==0:
            g=int(0)
            for ele in range (0,lenP-1):
                eleO=P[ele]
                if eleO>0:
                    g=g+1
            manareq=g+1
            break
        elif ele1==ele2:
            manareq=lenP
            break
        else:
            manareq=lenP+1
    m.append(manareq)
    n=n+1

for x in m:
    print (x)
