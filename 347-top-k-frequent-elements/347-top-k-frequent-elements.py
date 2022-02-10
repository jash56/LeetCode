import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        counter = collections.Counter(nums)
        count_list = [(-freq, -key) for key, freq in counter.items()]
        heapq.heapify(count_list)  
        
        answer = []
        for i in range(k):
            answer.append(-heapq.heappop(count_list)[1])
        return answer

        # counter = collections.Counter(nums)
        # count_list = [(freq, key) for key, freq in list(counter.items())]
        # ans = heapq.nlargest(k, count_list, key=lambda x: x[0])
        # return [j for i, j in ans]