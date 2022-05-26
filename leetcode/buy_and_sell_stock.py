prices_1 = [7, 1, 5, 3, 6, 4]
prices_2 = [7, 6, 4, 3, 1]


def buy_and_sell_one_pass(prices: list[int]) -> int:
    max_profit = 0
    min_buy = float('inf')

    for index, cur_price in enumerate(prices):
        min_buy = min(cur_price, min_buy)
        cur_profit = cur_price - min_buy
        max_profit = max(cur_profit, max_profit)

    return max_profit


print(buy_and_sell_one_pass(prices_1))
print(buy_and_sell_one_pass(prices_2))
