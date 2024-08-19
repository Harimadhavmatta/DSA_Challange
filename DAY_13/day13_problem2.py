def permutation(lis,l,n):
    if l==n:
        print("".join(lis))
    else:
        for i in range(l, n): 
            lis[l], lis[i] = lis[i], lis[l] 
            permutation(lis, l+1, n) 
            lis[l], lis[i] = lis[i], lis[l]
st="wxyz"
n=len(st)
lis=list(st)
permutation(lis,0,n)
