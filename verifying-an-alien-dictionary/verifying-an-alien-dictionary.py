class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        order_hash = {'' : 0}
        for index, alphabet in enumerate(order):
            order_hash[alphabet] = index+1
            
        for i in range(len(words)-1):
            temp1 = words[i]
            temp2 = words[i+1]
            temp = True
            for a in range(min(len(temp1), len(temp2))):
                if order_hash.get(temp1[a]) < order_hash.get(temp2[a]):
                    temp = False
                    break
                elif order_hash.get(temp1[a]) > order_hash.get(temp2[a]):
                    return False
            if temp and len(temp1) > len(temp2):
                return False
        return True
            