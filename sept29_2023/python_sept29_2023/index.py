import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = "Hello World"

def count_unique_characters(input_string):
    # Convert the input string to lowercase and remove whitespace
    cleaned_string = ''.join(input_string.split()).lower()

    # Initialize a dictionary to store character counts
    char_counts = {}

    # Count the occurrences of each character
    for char in cleaned_string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    # Count characters that occur exactly once
    unique_count = sum(1 for count in char_counts.values() if count == 1)

    return unique_count

# Example usage:
result = count_unique_characters(s)
print(result)  # Output: 5




