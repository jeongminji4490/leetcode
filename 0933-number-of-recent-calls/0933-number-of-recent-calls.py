class RecentCounter:
    requests = []

    def __init__(self):
        self.requests.clear()

    def ping(self, t: int) -> int:
        count = 0
        self.requests.append(t)
        first_t = t - 3000
        for request in self.requests:
            if request >= first_t and request <= t:
                count += 1
        return count


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)