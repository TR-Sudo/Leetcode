class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        // we wanna aim for O(n) for the best solution

        //start with a set (sets will not store duplicate values)

        var setValues= new Set()

        //add values from the array to the dict

        for(const num of nums){ // since there is only one loop its O(n) n depending on the number of items in array nums
           if(setValues.has(num)){
                return true; // if the value is already in the set return true
           }
           setValues.add(num)
        }
        //else return false
        return false;

    }
}
