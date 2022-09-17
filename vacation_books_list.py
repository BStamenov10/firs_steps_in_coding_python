all_pages = int(input())
pages_per_hour = int(input())
time = int(input())

result = (all_pages // pages_per_hour) / time
print(result)
