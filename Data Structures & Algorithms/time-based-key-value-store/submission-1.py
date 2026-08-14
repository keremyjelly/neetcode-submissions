class TimeMap:

    def __init__(self):
        self.ds = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.ds[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:

        l, r = 0, len(self.ds[key]) - 1
        res = ""
        while l <= r:
            mid = (l + r) // 2

            if self.ds[key][mid][0] <= timestamp:
                l = mid + 1
                res = self.ds[key][mid][1]
            else:
                r = mid - 1
        
        return res