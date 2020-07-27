MAxD = []
def inputconstrains():
    An = list(map(int,input().split()))
    Bn = list(map(int,input().split()))
    An.sort(reverse=True)
    t,S,ans,Ms,MAxs = 0,0,0,0,[]
    for x in range(len(An)-1,len(Bn)-1):
        if An[x]==An[x+1] and Bn[x]==Bn[x+1]:
            t= t+1
        if An[x]>=Bn[x]:
            Ms =Bn
        else:
            Ms = An
    if t==len(An):
        S = int(len(An))*Ms
        MAxs.append(int(S))
    for i in range(len(An)):
        if An[i]>=Bn[i]:
            S = S+int(Bn[i])
        else:
            S = S+int(An[i])

    return(S)

n,k =int(input()),[]
for i in range(n):
    T = int(input())
    t = inputconstrains()
    print(t)
