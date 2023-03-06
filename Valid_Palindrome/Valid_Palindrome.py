import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        splited=re.split(r'[^a-zA-Z0-9]',s)
        combinedStr=''.join(splited).lower()
        revStr=combinedStr[::-1].lower()

        if (s.isspace()==True):
            return True

        for x in range(len(revStr)):
            if revStr[x]!=combinedStr[x]:
                return False
        
        return True
