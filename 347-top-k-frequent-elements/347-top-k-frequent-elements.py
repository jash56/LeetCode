import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = collections.Counter(nums)
        print(counter)
        count_list = [(-freq, -key) for key, freq in list(counter.items())]
        
        heapq.heapify(count_list)
        print(count_list)
        answer = []
        for i in range(k):
            answer.append(-heapq.heappop(count_list)[1])
            print(answer)
        return answer