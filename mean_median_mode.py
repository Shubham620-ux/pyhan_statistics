# Function to calculate mean
def calculate_mean(numbers):
    total_sum = 0
    for num in numbers:
        total_sum += num
    mean = total_sum / len(numbers)
    return mean

# Function to calculate median
def calculate_median(numbers):
    numbers.sort()
    n = len(numbers)
    middle = n // 2
    
    # If the number of elements is odd, return the middle one
    if n % 2 == 1:
        return numbers[middle]
    # If the number of elements is even, return the average of the two middle ones
    else:
        return (numbers[middle - 1] + numbers[middle]) / 2

# Function to calculate mode
def calculate_mode(numbers):
    frequency = {}
    
    # Count the frequency of each number in the list
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    # Find the number(s) with the highest frequency
    max_frequency = max(frequency.values())
    mode = [key for key, value in frequency.items() if value == max_frequency]
    
    # Return the mode; if multiple values have the same frequency, return all of them
    if len(mode) == 1:
        return mode[0]  # Single mode
    else:
        return mode     # Multiple modes

# Example usage:
numbers = [5, 2, 7, 3, 9, 2, 5, 5, 2, 7]

mean = calculate_mean(numbers)
median = calculate_median(numbers)
mode = calculate_mode(numbers)

print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
