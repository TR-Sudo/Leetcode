class Solution(object):
    #Solution using a hashmap and time complexity of O(M*N)
    #M is the length of the array and N is the average length of each string
    def groupAnagrams(self, strs):
        rList = defaultdict(list)# defining dictionary with values as a list
        for s in strs:
            counts=[0]*26 # a...z
            for c in s:
                counts[ord(c) - ord("a")]+=1 #ord finds the asci value of c and -80 (asci value of a), ex=> a=80-80=0, b=81-80=1
            rList[tuple(counts)].append(s)#Tuples are immutable, meaning that once a tuple has been created, the items in it can't change.
        return rList.values()