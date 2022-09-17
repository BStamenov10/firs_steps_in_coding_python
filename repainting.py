nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())

sum_nylon = (nylon + 2) * 1.5
sum_paint = (paint + (paint/10)) * 14.5
sum_thinner = thinner * 5
sum_for_bag = 0.40

all_price = sum_nylon + sum_paint + sum_thinner + sum_for_bag
sum_for_workers = ((all_price * 30)/100) * hours
overall = all_price + sum_for_workers
print(f" сумата на всички разходи {overall}")
