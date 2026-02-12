import math

def merge(a,b):
    n,m=len(a),len(b)
    gap=math.ceil((n+m)/2)

    while gap>0:
        i=0
        while i+gap<n+m:
            j=i+gap
            if i<n and j<n:
                if a[i]>a[j]:
                    a[i],a[j]=a[j],a[i]
            elif i<n:
                if a[i]>b[j-n]:
                    a[i],b[j-n]=b[j-n],a[i]
            else:
                if b[i-n]>b[j-n]:
                    b[i-n],b[j-n]=b[j-n],b[i-n]
            i+=1
        gap=0 if gap==1 else math.ceil(gap/2)
