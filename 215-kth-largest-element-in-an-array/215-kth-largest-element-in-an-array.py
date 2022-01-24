class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap, nums[i])
            if i >= k:
                heapq.heappop(heap)
        return heapq.heappop(heap)
        
        
        
#         nums = [-x for x in nums]
#         heapq.heapify(nums)
        
#         for i in range(k-1):
#             heapq.heappop(nums)
        
#         return - heapq.heappop(nums)
    
        #return heapq.nlargest(k, nums)[-1]