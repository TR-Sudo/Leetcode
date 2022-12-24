class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #Solution using a hash set O(N)
        hash=set()
        for x,val in enumerate(nums):
            if val in hash:
                return True
            hash.add(val)
        return False