object Solution {
    def missingNumber(nums: Array[Int]): Int = {
        var temp = Range(0,nums.length+1).sum
        var num = nums.toSet.sum
        temp-num
    }
}