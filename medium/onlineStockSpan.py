class StockSpanner:

    def __init__(self):
        self.span_stack = []

    def next(self, price: int) -> int:
        res = 1
        while self.span_stack and self.span_stack[-1][0] <= price:
            res += self.span_stack.pop()[1]
        self.span_stack.append([price, res])
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)