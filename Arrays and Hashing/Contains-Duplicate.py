# https://leetcode.com/problems/contains-duplicate/


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        l =  len(nums)
        if l < 2:
            return False
        nums.sort()
        for i in range(l-1):
            if nums[i] == nums[i+1]:
                return True
        return False
    
    
    # Another Method  -- Apply hashtable O(n)
    # hashNum = {}
    # for i in nums:
    #     if i not in hashNum:
    #         hashNum[i] = 1
    #     else:
    #         return True
    # return False
