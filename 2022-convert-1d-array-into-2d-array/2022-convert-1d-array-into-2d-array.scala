object Solution {
    def construct2DArray(original: Array[Int], m: Int, n: Int): Array[Array[Int]] = {
        if (original.length != (m*n)) {
            Array.ofDim[Int](0, 0)
        }
        else{
            val ans = Array.ofDim[Int](m, n)
            var idx = 0
            for (i <- 0 to m-1) {
                for (j <- 0 to n-1) {
                    ans(i)(j) = original(idx) 
                    idx = idx + 1
                }
            }
            ans
        }   
    }
}