class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i,value in enumerate(nums):
            new_nums = nums.copy()
            new_nums.pop(i)
            mul = 1
            for new_num in new_nums:
                mul *= new_num
            res.append(mul)
        return res
            

        