function twoSum(nums: number[], target: number): number[] {
    for (let i = 0; i < nums.length; i++) {
        for (let j = i; j < nums.length; j++) {
            if (nums[i] + nums[j + 1] === target) {
                return [i,j+1]
            }
        }
    }
    return []
};