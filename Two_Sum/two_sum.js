class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        
        // goal is O(n)

        // lets use a hashmap and map the key to the position in the array

        var hm=new Map()

        // we will iterate over the array nums and add it to the hashmap

        for (var x=0;x<nums.length;x++){
            if(hm.has(target-nums[x])){
                return [hm.get(target - nums[x]), x];
            }
            hm.set(nums[x], x); //key is int at nums[x] and value is x which is position
        }
        return null
    }
}
