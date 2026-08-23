from sortedcontainers import SortedDict
class TimeMap:

    def __init__(self):
        self.map = defaultdict(SortedDict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key][timestamp] = value
    
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ''
        timestamps = self.map[key]
        position = timestamps.bisect_right(timestamp) - 1
        if position >= 0:
            closest = timestamps.iloc[position]
            return timestamps[closest]
        return ''
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)