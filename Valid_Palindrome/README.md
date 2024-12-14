``` JavaScript
class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        // goal O(n) time and O(1)

        // lets use and array and add values from outside in using two pointers
        

        //strip all non alphanumeric values from s

        
        var str = s.replaceAll(/[^a-zA-Z0-9]/g, "").toLocaleLowerCase();

        for(var x =0; x<str.length;x++){
            if(str[x]!=str[(str.length-1)-x]){// will end on O(1) 
                return false
            }
        }
        return true
    }
}

```