class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        index_hash = {}
        for i in range(len(numbers)):
            index_hash[numbers[i]] = i + 1
            
        for i in range(len(numbers)):
            complement = target - numbers[i]
            if complement in index_hash:
                return [i+1, index_hash[complement]]