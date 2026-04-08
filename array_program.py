# Find largest element in an array

arr = [10, 25, 7, 99, 3]

largest = arr[0]

for num in arr:
    if num > largest:
        largest = num

print("Largest element is:", largest)
