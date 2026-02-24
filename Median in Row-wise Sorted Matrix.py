import heapq

def matrix_median(mat):
    arr = []
    for row in mat:
        arr.extend(row)
    arr.sort()
    return arr[len(arr)//2]