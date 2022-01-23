class MedianFinder:

    def __init__(self):
        self.num_list = []

    def addNum(self, num: int) -> None:
        self.num_list.append(num)

    def findMedian(self) -> float:
        self.num_list.sort()
        n = len(self.num_list)
        if n % 2 == 0:
            n = int(n / 2)
            return ((self.num_list[n] + self.num_list[n-1]) / 2)
        else:
            return self.num_list[n // 2]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()