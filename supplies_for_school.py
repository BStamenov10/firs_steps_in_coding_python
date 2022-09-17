pens = int(input())
markers = int(input())
detergent_lt = int(input())
discount_percent = int(input())

price_pens = pens * 5.80
price_markers = markers * 7.20
price_detergent = detergent_lt * 1.20

all_price = price_pens + price_markers + price_detergent
discount = (discount_percent/100)
sum = all_price - (all_price * discount)
print(sum)
