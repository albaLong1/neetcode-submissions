class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        streak = 1
        length = len(self.stack)
        copy = self.stack[:length]
        while len(copy) != 0:
            value = copy.pop()
            if value <= price:
                streak += 1
            else:
                break
        self.stack.append(price)
        return streak


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)