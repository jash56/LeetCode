class NumArray(_nums: Array[Int]) {

    def sumRange(left: Int, right: Int): Int = {
        var ans = 0
        Range(left, right+1).foreach(ans += _nums(_))
        ans
    }

}

/**
 * Your NumArray object will be instantiated and called as such:
 * var obj = new NumArray(nums)
 * var param_1 = obj.sumRange(left,right)
 */