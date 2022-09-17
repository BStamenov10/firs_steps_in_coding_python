length = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume = length * width * height
volume_lt = volume / 1000

acc_volume = volume_lt * (percent / 100)
result = volume_lt - acc_volume
print(result)
