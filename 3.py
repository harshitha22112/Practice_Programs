numbers = [4,3,5,7,8,9]
target = int(input("Enter number:"))
for i in range(len(numbers)):
    for j in range(len(numbers)-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
            print(numbers)