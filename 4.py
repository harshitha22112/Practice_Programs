numbers = [10,20,30,40,10]
for num in set(numbers):
    if numbers.count(num) > 1:
        print(num)