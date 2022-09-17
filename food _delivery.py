chicken_menus = int(input())
fish_menus = int(input())
vegetarian_menus = int(input())

price_chicken = chicken_menus * 10.35
price_fish = fish_menus * 12.40
price_vegetarian = vegetarian_menus * 8.15

total_price_menus = price_fish + price_chicken + price_vegetarian
dessert = (total_price_menus * 20) / 100
delivery = 2.50

total_price = total_price_menus + delivery + dessert
print(total_price)
