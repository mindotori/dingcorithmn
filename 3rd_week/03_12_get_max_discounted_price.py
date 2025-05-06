shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]

# <정렬>
# 가장 비싼 금액이 가장 많이 할인을 받으면 된다. (내림차순 정렬 사용)
# 할인 배열 원소가 price 원소보다 적으면 할인 못받는 원소 발생 => 원가로 넣어줘야함
def get_max_discounted_price(prices, coupons):
    prices.sort(reverse=True) #내림차순
    coupons.sort(reverse=True)

    # 사용할 인덱스 선언
    price_index = 0
    coupon_index = 0
    max_discounted_price = 0 #여기에 할인율 적용한 가격 누적시키자 (총 가격)

    while price_index < len(prices) and coupon_index < len(coupons): # 현재 가격과 쿠폰이 모두 배열 내의 원소일때까지
        discounted_price =  prices[price_index] * (100 - coupons[coupon_index]) / 100
        max_discounted_price += discounted_price # 금액 누적
        price_index += 1
        coupon_index += 1

    while price_index < len(prices): #즉, 현재 price_index가 prices 길이 범위 내라면,
        max_discounted_price += prices[price_index]
        price_index += 1

    return max_discounted_price






print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))