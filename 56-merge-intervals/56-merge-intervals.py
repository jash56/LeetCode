class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if len(intervals) == 1: return intervals
        intervals = sorted(intervals, key=lambda x: x[0])
        
        final_intervals = [intervals[0]]

        for interval in intervals:
            
            if interval[0] <= final_intervals[-1][1]:
                final_intervals[-1][1] = max(interval[1], final_intervals[-1][-1])
            else:
                final_intervals.append(interval)
                
        return final_intervals