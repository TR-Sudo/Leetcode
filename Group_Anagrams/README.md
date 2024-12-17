``` JavaScript
class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {

        //dictionaries are good for grouping
        var dict={}
       
        for (let word of strs){
            let sorted=word.split("").sort().join("")
            if(dict[sorted])//if the key is available
            {
                dict[sorted].push(word)//adds the str at x if it's already available at dict
                
            }else{
                dict[sorted] = [word]
            }
            
        }
        return Object.values(dict)
    }
}

```