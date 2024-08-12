class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for i in range(len(nums)):
            hm[nums[i]] = i
        
        for i in range(len(nums)):
            y = target - nums[i]
        
            if y in hm and hm[y] != i:
                return [i,hm[y]]