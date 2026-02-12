def is_subset(a,b):
    freq={}
    for x in a:
        freq[x]=freq.get(x,0)+1
    for x in b:
        if freq.get(x,0)==0:
            return False
        freq[x]-=1
    return True
