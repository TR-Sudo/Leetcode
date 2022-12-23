class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
       #O(N^2) solution
        for x in range(len(nums)):
            for y in range(x+1,len(nums)):
                if(x!=y):
                    if (nums[x]+nums[y]==target):
                        return [x,y]
        return None

        #O(N) solution using dictionary to store the complements of nums value
        cMap=dict()
        for x,arrNum in enumerate(nums):
            if arrNum in cMap:
                return [cMap[arrNum],x]
            cMap[target-arrNum]=x
        return None