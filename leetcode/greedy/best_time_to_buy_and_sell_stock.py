def best_time_to_buy_and_sell_stock(prices: list[int]) -> int:
    buy_price = prices[0]
    profit = 0

    for price in prices:
        buy_price = min(price, buy_price)
        profit = max(price - buy_price, profit)

    return profit


input_1 = [7, 1, 5, 3, 6, 4]
input_2 = [7, 6, 4, 3, 1]

print(best_time_to_buy_and_sell_stock(input_1))
print(best_time_to_buy_and_sell_stock(input_2))
