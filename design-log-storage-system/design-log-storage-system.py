from collections import defaultdict

class LogSystem:

    def __init__(self):
        self.log_system = defaultdict(set) #log system hash table
        self.granularity_index = {'Year':3, 'Month':6, 'Day':9, 'Hour':12, 'Minute':15, 'Second':18} #format is year:month:day:hour:minute:second --> xxxx:xx:xx:xx:xx:xx

    def put(self, id: int, timestamp: str) -> None:
        self.log_system[timestamp].add(id)
        print(self.log_system)

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        
        answer = []
        start = start[:self.granularity_index[granularity]+1]   
        end = end[:self.granularity_index[granularity]+1]
        start = int(re.sub(':', '', start))
        end = int(re.sub(':', '', end))
        
        for time_stamp, id_list in self.log_system.items():
            time_stamp = time_stamp[:self.granularity_index[granularity]+1]
            time_stamp = int(re.sub(':', '', time_stamp))
            if start <= time_stamp <= end:
                answer.extend(id_list)
                
        return answer
                
        

# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)