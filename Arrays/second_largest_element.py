arr = list(map(int, input("Enter the elements of the array separated by space: ").split()))
unique_elements = list(set(arr))
unique_elements.sort(reverse=True)

if len(unique_elements) < 2:
    print("The array does not have enough elements to determine the second largest.")
else:
    print("Second largest element:", unique_elements[1])
