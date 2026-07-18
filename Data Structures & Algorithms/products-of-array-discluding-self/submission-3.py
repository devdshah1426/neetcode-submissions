class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        res = [1] * n
        
        # Left pass — fill res[i] with product of everything LEFT of i
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        
        # Right pass — multiply res[i] by product of everything RIGHT of i
        suffix = 1
        for i in range(n-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        
        return res