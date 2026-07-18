class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = []
        for idx,i in enumerate(nums):
            num_2 = target-i
            seen.append(idx)
            if num_2 in nums and idx not in seen:
                return [idx,nums.index(num_2)]
            else:
                continue

        