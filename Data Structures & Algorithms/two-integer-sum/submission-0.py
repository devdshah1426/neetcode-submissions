class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx,i in enumerate(nums):
            num_2 = target-i
            if num_2 in nums:
                return [idx,nums.index(num_2)]
            else:
                continue

        