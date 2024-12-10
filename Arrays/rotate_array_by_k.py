arr = list(map(int, input("Enter the elements of the array separated by space: ").split()))
k = int(input("Enter the number of positions to rotate by: "))
k = k % len(arr)
rotated_array = arr[-k:] + arr[:-k]

print("Array after rotation:", rotated_array)
