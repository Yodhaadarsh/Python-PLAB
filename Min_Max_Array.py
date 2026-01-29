#given an array arr[].your task is to find the minimum and maximum elements in the array.
class Solution:
    def findMinMax(self, arr):
        min=arr[0]
        max=arr[0]

        for num in arr:
            if num<min:
                min=num
            if num>max:
                max=num
        return [min, max]
obj=Solution()
arr = [3,5,1,8,2,75,3,6,73,94]
result = obj.findMinMax(arr)
print("Min:", result[0])
print("Max:", result[1])