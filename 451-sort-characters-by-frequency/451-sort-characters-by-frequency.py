class Solution:
    def frequencySort(self, s: str) -> str:
        ans = ''
        counter = {}
        for i in s:
            counter[i] = counter.get(i, 0) + 1
        counter_list = list(counter.items())
        counter_list.sort(key=lambda x: x[1], reverse=True)
        for char, freq in counter_list:
            substring = [char] * freq
            ans = ans + ''.join(substring)
        return ans