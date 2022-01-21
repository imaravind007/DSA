def search(nums, target):
        left = 0
        right = len(nums)-1
        mid = 0
        while left <= right:
            mid = (right + left) //2
            if nums[mid] == target:
                return mid 
            if nums[mid] < target:
                left = mid +1 
            else:
                right = mid -1 
        return -1
nums = [1,2,3,4,5,6,7]
target = 7
output = search(nums, target)
print(output)