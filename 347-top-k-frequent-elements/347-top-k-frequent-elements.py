import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
#         counter = collections.Counter(nums)
#         count_list = [(-freq, -key) for key, freq in list(counter.items())]
#         heapq.heapify(count_list)  
        
#         answer = []
#         for i in range(k):
#             answer.append(-heapq.heappop(count_list)[1])
#         return answer
        counter = collections.Counter(nums)
        print(counter)
        count_list = [(freq, key) for key, freq in list(counter.items())]
        print(count_list)
        ans = heapq.nlargest(k, count_list, key=lambda x: x[0])
        print(ans)
        return [j for i, j in ans]