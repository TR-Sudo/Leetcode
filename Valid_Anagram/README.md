``` Python
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        smap,tmap={},{}
        for s,val in enumerate(s):
            smap[val]=smap.get(val,0)+1

        for t,val in enumerate(t):
            tmap[val]=tmap.get(val,0)+1
        return tmap==smap 
```
