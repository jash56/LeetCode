class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = collections.Counter(nums)
        
        count_list = list(counter.items())
        count_list.sort(key=lambda x: x[1], reverse=True)

        ans = []
        for i in count_list[:k]:
            ans.append(i[0])
        return ans