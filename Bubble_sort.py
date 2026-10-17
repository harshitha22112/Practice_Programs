numbers = [6,4,3,7,2]
for i in range(len(numbers)):
    for j in range(len(numbers)-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j +1] = numbers[j+1], numbers[j]
            print("Sorted:", numbers)