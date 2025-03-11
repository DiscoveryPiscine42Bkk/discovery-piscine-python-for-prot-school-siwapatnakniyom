# Original array
original_array = [2, 8, 9, 48, 8, 22, -12, 2]

# Filter values greater than 5 and remove duplicates while maintaining order
filtered_array = []
seen = set()

for num in original_array:
    if num > 5 and num not in seen:
        filtered_array.append(num)
        seen.add(num)

# Print the result
print("Filtered unique values greater than 5:", filtered_array)
