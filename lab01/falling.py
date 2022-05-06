def falling(n,k):
    res = 1
    i = 1
    while i<=k:
        res = res*n
        n=n-1
        i=i+1
    return res
