class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums1_copy = nums1[:m]
        j = k = 0
        for i in range(n + m):
            if k >= n or (j < m and nums1_copy[j] < nums2[k]):
                nums1[i] = nums1_copy[j]
                j += 1
            elif k < n:
                nums1[i] = nums2[k]
                k += 1
        
            
                
            
            
            
            