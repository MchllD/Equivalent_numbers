# Exercise 5: Check if the first and last number of a list is the same
# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.


# pseudocode

# Function to check the similarity of the first and last numbers in a list
# Get the first and last numbers from the list
# Check if the first and last numbers are the same
# Return True to indicate successful match
# Return False to indicate no match
# Sample 1
# Sample 2
# Sample 3
# Call the check_first_last_similarity function with the first, second & third sample


# ***************************************************** actual code *****************************************************************
# Function to check the similarity of the first and last numbers in a list
def check_first_last_similarity(numbers):
    print("\nChecking the mystery and similarity of the first and last numbers in the list:", numbers)
    
# Get the first and last numbers from the list
    first_number = numbers[0]
    last_number = numbers[-1]
    
# Check if the first and last numbers are the same
# Return True to indicate successful match
# Return False to indicate no match
    if first_number == last_number:
        print("✨ Result: Congrats! You uncovered the secret: the first and last numbers match! ✨")
        return True
    else:
        print("🕵️‍♂️ Result: Oops! The mystery continues - the first and last numbers are different. Keep exploring! 🕵️‍♂️")
        return False

# Sample 1
magical_numbers_1 = [7, 14, 21, 28, 7]
print("\nSample 1 -", check_first_last_similarity(magical_numbers_1))

# Sample 2
magical_numbers_2 = [10, 20, 30, 40, 50]
print("\nSample 2 -", check_first_last_similarity(magical_numbers_2))


# Sample 3
# Call the check_first_last_similarity function with the first, second & third sample
