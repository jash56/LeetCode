from collections import defaultdict
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        
        user_uam = defaultdict(set) #hash table for each user and corresponding minute set for which they are active
        
        #populate hash table for each user and their active minute set
        for user_id, time in logs:  
            user_uam[user_id].add(time)

        answer = [0] * k  #list of number of users whose uam is j
        
        #iterate over the active minute list for each user and populate answer list
        for value in user_uam.values():
            answer[len(value)-1] += 1
            
        return answer