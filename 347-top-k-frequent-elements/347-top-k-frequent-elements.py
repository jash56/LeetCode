class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = collections.Counter(nums)
        
        count_list = list(counter.items())
        count_list.sort(key=lambda x: x[1], reverse=True)

        for i in range(k):
            count_list[i] = count_list[i][0]
        return count_list[:k]