/**
*   Return the second largest number in the array.
*   @param {Number[]} nums - An array of numbers.
*   @return {Number} The second largest number in the array.
**/
function getSecondLargest(nums) {
    // Complete the function
    nums.sort(function(x, y) { return x < y; });
    let i = 1;
    while (i >= 0 && nums[0] == nums[i]) {
        i++;
    }
    return nums[i];
}