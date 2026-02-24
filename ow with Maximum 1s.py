def row_with_max_ones(mat):
    max_count = 0
    index = -1
    
    for i in range(len(mat)):
        count = sum(mat[i])
        if count > max_count:
            max_count = count
            index = i
    
    return index