class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        n=len(nums)
        start = 0 
        for i in range(0,n-1):
            start+=1
            if nums[i]==nums[start]:
                return True

        return False