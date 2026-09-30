class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store.setdefault(key, []).append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        arr = self.store.get(key, [])
        l, h = 0, len(arr) - 1

        res = ""

        while l <= h:
            mid = (l + h) // 2
            if(arr[mid][0] <= timestamp):
                res = arr[mid][1]
                l = mid+1

            else:
                h = mid -1

        return res

