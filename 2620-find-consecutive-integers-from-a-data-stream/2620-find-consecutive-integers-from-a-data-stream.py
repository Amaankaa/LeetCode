class DataStream:

    def __init__(self, value: int, k: int):
        self.window = deque()
        self.k = k
        self.value = value
        self.count = 0

    def consec(self, num: int) -> bool:
        self.window.append(num)
        if num == self.value:
            self.count += 1

        if len(self.window) > self.k:
            a = self.window.popleft()
            if a == self.value:
                self.count -= 1
        
        return len(self.window) == self.k and self.count == self.k


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)