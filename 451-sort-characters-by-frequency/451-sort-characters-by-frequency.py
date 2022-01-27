class Solution:
    def frequencySort(self, s: str) -> str:
        ans = ''
        counter = {}
        for i in s:
            counter[i] = counter.get(i, 0) + 1
        
        counter = [[val, key] for key, val in counter.items()]
        counter.sort(reverse=True)
        ans = [char * freq for freq, char in counter]
        return ''.join(ans)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        counter_list = list(counter.items())
        counter_list.sort(key=lambda x: x[1], reverse=True)
        string_builder = []
        for char, freq in counter_list:
            string_builder.append(char * freq)
        return ''.join(string_builder)