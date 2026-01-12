def longest_subarray_with_given_sum_k(nums,k):
        n = len(nums) 
        maxLength = 0
        for i in range(n):
            for j in range(i, n):
                currentSum = 0
                for i in range(i, j + 1):
                    currentSum += nums[i]

                if currentSum == k:
                    maxLength = max(maxLength,j- i + 1)
        return maxLength

