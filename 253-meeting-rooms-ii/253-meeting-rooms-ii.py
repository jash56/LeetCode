import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x: x[0])
        
        in_use = [intervals[0][1]]
        room_count = 1
        
        for interval in intervals[1:]:
            if interval[0] >= in_use[0]:
                heapq.heappop(in_use)
                heapq.heappush(in_use, interval[1])
            else:
                heapq.heappush(in_use, interval[1])
                room_count += 1
                
        return room_count