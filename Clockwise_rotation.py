def rotate_array(arr):
    if len(arr) == 0:
        return arr
    return [arr[-1]] + arr[:-1]


# Example
arr = [1, 2, 3, 4, 5]
print(rotate_array(arr))  # Output: [5, 1, 2, 3, 4]