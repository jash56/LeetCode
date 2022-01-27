class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        
        i = len(nums1)
        m -= 1
        n -= 1
        while m >= 0 and n >= 0:
            print(i, nums1)
            i -= 1
            
            if nums1[m] < nums2[n]:
                nums1[i] = nums2[n]
                n -= 1
            else:
                nums1[i] = nums1[m]
                m -= 1
        
        while n >= 0:
            i -= 1
            nums1[i] = nums2[n]
            n -= 1
            
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # j = m - 1
        # k = n - 1
        # for i in range(n + m - 1, -1, -1):
        #     if k < 0:
        #         break
        #     if j >= 0 and nums1[j] > nums2[k]:
        #         nums1[i] = nums1[j]
        #         j -= 1          
        #     else:
        #         nums1[i] = nums2[k]
        #         k -= 1
            
        
            
                
            
            
            
            