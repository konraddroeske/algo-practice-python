prices_1 = [7, 1, 5, 3, 6, 4]
prices_2 = [7, 6, 4, 3, 1]


def buy_and_sell_one_pass(prices: list[int]) -> int:
    min_buy = prices[0]
    max_profit = 0

    for index, cur_price in enumerate(prices):
        if cur_price < min_buy:
            min_buy = cur_price

        cur_profit = cur_price - min_buy

        if cur_profit > max_profit:
            max_profit = cur_profit

    return max_profit


print(buy_and_sell_one_pass(prices_1))
print(buy_and_sell_one_pass(prices_2))
