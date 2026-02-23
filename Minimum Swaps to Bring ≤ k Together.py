def min_swaps(arr, k):
    count = sum(1 for num in arr if num <= k)
    
    bad = sum(1 for num in arr[:count] if num > k)
    ans = bad
    
    for i in range(len(arr) - count):
        if arr[i] > k:
            bad -= 1
        if arr[i + count] > k:
            bad += 1
        ans = min(ans, bad)
    
    return ans