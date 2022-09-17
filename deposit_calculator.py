deposit = float(input())
deadline = int(input())
annual_interest_rate = float(input())

interest = deposit * (annual_interest_rate / 100)

month = interest / 12
sum = deposit + deadline * month
print(sum)