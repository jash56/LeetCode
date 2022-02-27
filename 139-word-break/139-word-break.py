class Solution:
    
    def applepie_two(self, input_string, english_dict, memo):  
  
        if not input_string:
            return True
        
        if input_string in memo:
            return memo[input_string]
        
        for idx in range(len(input_string)+1):       
            word1 = input_string[:idx]  
            if word1 in english_dict:
                if self.applepie_two(input_string[idx:], english_dict, memo):
                    memo[input_string] = True
                    return True
                else:
                    memo[input_string] = False
            
    def wordBreak(self, s: str, wordDict: List[str]) -> bool: 
        memo = {}
        return self.applepie_two(s, wordDict, memo)
        