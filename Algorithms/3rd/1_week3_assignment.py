shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices, coupons):
    prices.sort(reverse=True)
    coupons.sort(reverse=True)
    p_index = 0
    c_index = 0
    get_price = 0
    while p_index < len(prices) and c_index < len(coupons):
        print(p_index)
        get_price += prices[p_index] * (100 - coupons[c_index]) / 100
        p_index += 1
        c_index += 1
    while p_index < len(prices):
        get_price += prices[p_index]
        p_index += 1

    return get_price



print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))