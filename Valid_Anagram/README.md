``` JavaScript
class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        // store each value into a hash set
        // goal is O(n + m) n is size of s and m is size of t

        var hs1= new Map()
        var hs2= new Map()


        if(s.length!=t.length)return false;// easy check if both s and t are equal in length

        for (var x=0;x<s.length;x++){
            hs1[s[x]]=1+(hs1[s[x]] || 0)// default to 0 if the key doesnt exist already and add 1 
            hs2[t[x]]=1+(hs2[t[x]] || 0)
        }
        for (const x in hs1){
            if(hs1[x]!=hs2[x]){// if the value of hs1 as key x is not = to hs2 at key x return false
                return false
            }
        }
        return true
        

    }
}
```
