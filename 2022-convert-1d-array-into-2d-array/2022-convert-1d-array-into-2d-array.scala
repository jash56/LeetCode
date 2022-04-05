object Solution {
    def construct2DArray(original: Array[Int], m: Int, n: Int): Array[Array[Int]] = {
        if (original.length != (m*n)) {
            Array.ofDim[Int](0, 0)
        }
        else {
            val ans = Array.ofDim[Int](m, n)
            for (i <- 0 to original.length-1) {
                // println(i/m, i%n, i);
                ans(i/n)(i%n) = original(i) }
            ans
        }   
    }
}