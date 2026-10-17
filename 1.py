numbers = [10,20,30,40,50]
target = int(input("Enter number:"))
for i in range(len(numbers)):
    if numbers[i] == target:
        print("Found")
        break
else:
    print("Not found")