# Demonstrate List Slicing

numbers = list(range(1,11))
print("Original list: " ,numbers)
a= "Extracted first five elements:"
print(a, numbers[0:5])

numbers.reverse()
b= "Reversed extracted elements: "
print(b ,numbers[5:11])