square_metres = float(input())
price_one_square_metres = 7.61

result = square_metres * price_one_square_metres
discount = result * 0.18
final_price = result - discount

print(f"The discount is: {final_price} lv.")
print(f"The final price is: {discount} lv.")
