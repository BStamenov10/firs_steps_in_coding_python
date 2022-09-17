year_tax = int(input())

shoes_price = year_tax - year_tax * 0.4
outfit_price = shoes_price - shoes_price * 0.2
ball_price = outfit_price / 4
accessories_price = ball_price / 5

total_price = year_tax + shoes_price + outfit_price + ball_price + accessories_price
print(total_price)