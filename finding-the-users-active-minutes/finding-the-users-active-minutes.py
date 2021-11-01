class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        
        answer = [0] * k  #list of number of users whose uam is j
        user_uam = {} #hash table for each user and corresponding minute list for which they are active
        
        #populate hash table for each user and their active minute list
        for user_id, time in logs:  
            active_min_list = user_uam.get(user_id, [])
            if time not in active_min_list:
                active_min_list.append(time)
            user_uam[user_id] = active_min_list

        #iterate over the active minute list for each user and populate answer list
        for value in user_uam.values():
            answer[len(value)-1] += 1
            
        return answer