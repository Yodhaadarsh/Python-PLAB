def is_palindrome(arr):
    for num in arr:
        if str(num) != str(num)[::-1]:
            return False
    return True