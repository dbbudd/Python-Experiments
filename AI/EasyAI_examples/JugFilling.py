class jug:
    def __init__(self, size):
        self.size = size
        self.volume = 0
        self.waste = 0
 
    def empty(self):
        self.waste = self.waste + self.volume
        self.volume = 0
 
    def fill(self):
        self.volume = self.size
 
    def is_full(self):
        return self.volume == self.size
 
    def get_unused_volume(self):
        return self.size - self.volume
 
    def pour(self, jug):
        if self != jug and jug.is_full() == False:
            if jug.get_unused_volume() >= self.volume: # Receiving jug has enough spare volume for all of the pouring jug's contents.
                jug.volume = jug.volume + self.volume
                self.volume = 0
            else: # Receiving jug does not have enough spare volume for all of the pouring jug's contents.
                self.volume = self.volume - jug.get_unused_volume()
                jug.volume = jug.size

    @staticmethod 
    def solve_4_litre_puzzle_method_1():
        # Setup two jugs - one 3 litre and one 5 litre.
        jug3 = jug(3)
        jug5 = jug(5)
 
        # Fill the 5 litre jug and pour into the 3 litre jug.
        jug5.fill()
        assert(jug5.volume == 5)
        jug5.pour(jug3)
        assert(jug5.volume == 2)
        assert(jug3.volume == 3)
 
        # Empty the 3 litre jug.
        jug3.empty()
        assert(jug3.volume == 0)
 
        # Pour the 2 litres from the 5 litre jug into the 3 litre jug.
        jug5.pour(jug3)
        assert(jug5.volume == 0)
        assert(jug3.volume == 2)
 
        # Fill the 5 litre jug and pour into the 3 litre jug.
        jug5.fill()
        assert(jug5.volume == 5)
        jug5.pour(jug3)
        assert(jug3.volume == 3)
 
        assert(jug5.volume == 4)
 
        assert(jug3.waste + jug5.waste == 3)
 
    @staticmethod
    def solve_4_litre_puzzle_method_2():
        # Setup two jugs - one 3 litre and one 5 litre.
        jug3 = jug(3)
        jug5 = jug(5)
 
        # Fill the 3 litre jug and pour into the 5 litre jug.
        jug3.fill()
        assert(jug3.volume == 3)
        jug3.pour(jug5)
        assert(jug3.volume == 0)
        assert(jug5.volume == 3)
 
        # Fill the 3 litre jug and pour into the 5 litre jug (again), leaving 1 litre in the 3 litre jug.
        jug3.fill()
        assert(jug3.volume == 3)
        jug3.pour(jug5)
        assert(jug3.volume == 1)
        assert(jug5.volume == 5)
 
        # Empty the 5 litre jug.
        jug5.empty()
        assert(jug5.volume == 0)
 
        # Pour the remaining 1 litre from the 3 litre jug into the 5 litre jug.
        jug3.pour(jug5)
        assert(jug3.volume == 0)
        assert(jug5.volume == 1)
 
        # Fill the 3 litre jug and pour into the 5 litre jug to make exactly 4 litres.
        jug3.fill()
        assert(jug3.volume == 3)
        jug3.pour(jug5)
        assert(jug3.volume == 0)
 
        assert(jug5.volume == 4)
 
        assert(jug3.waste + jug5.waste == 5)
 
# An algorithm to solve the maximising the profit of yesterday's stock prices.
def get_max_profit_big_o_nn(stock_price):
    max_profit = 0
    max_price = stock_price[0]
    min_price = stock_price[0]
    for i in range(0, len(stock_price)):
        min_price = min(stock_price[i], min_price)
        max_price = stock_price[i]
        for j in range(i, len(stock_price)):
            max_price = max(stock_price[j], max_price)
        max_profit = max(max_price - min_price, max_profit)
    return max_profit

def get_max_profit_big_o_n(stock_price):
    max_profit = 0
    min_price = stock_price[0]
    for i in range(0, len(stock_price)):
        temp_profit = stock_price[i] - min_price
        max_profit = max(temp_profit, max_profit)
        min_price = min(stock_price[i], min_price)
    return max_profit

if __name__ == "__main__":
    jug.solve_4_litre_puzzle_method_1()
    jug.solve_4_litre_puzzle_method_2()

    # Setting stock prices at constant time intervals.
    stock_price_random   = [12, 14, 20, 10, 5, 8, 15, 21, 17]
    stock_price_increase = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    stock_price_decrease = [9, 8, 7, 6, 5, 4, 3, 2, 1]

    assert(get_max_profit_big_o_nn(stock_price_random) == 16)
    assert(get_max_profit_big_o_nn(stock_price_increase) == 8)
    assert(get_max_profit_big_o_nn(stock_price_decrease) == 0)

    assert(get_max_profit_big_o_n(stock_price_random) == 16)
    assert(get_max_profit_big_o_n(stock_price_increase) == 8)
    assert(get_max_profit_big_o_n(stock_price_decrease) == 0)

    input("Press <Enter>")