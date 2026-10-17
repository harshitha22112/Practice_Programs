numbers = [22,12,33,67,46,98]
even = 0
odd = 0
for i in numbers:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
        print(even)
        print(odd)