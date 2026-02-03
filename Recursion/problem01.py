#Reverse an Array Using Recursion

nums = [0,4,6,5,7,8]

left = 0
right = 5

def reverse(nums,left,right):
    if left>=right:
        return
    nums[left],nums[right] = nums[right],nums[left]
    reverse(nums,left+1,right-1)

def reverse_array(nums,left,right):
    reverse(nums,left,right)

nums = [0,4,6,5,7,8]
reverse_array(nums, 0, len(nums)-1)
print(nums)
