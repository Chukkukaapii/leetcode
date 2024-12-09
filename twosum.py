def two_sum(nums, target):
    # Create a dictionary to store the numbers and their indices
    num_dict = {}
    
    # Loop through the list of numbers
    for i, num in enumerate(nums):
        # Calculate the complement (the number that needs to be added to num to reach the target)
        complement = target - num
        
        # If the complement is already in the dictionary, return its index and the current index
        if complement in num_dict:
            return [num_dict[complement], i]
        
        # Otherwise, store the number and its index in the dictionary
        num_dict[num] = i
    
    # If no solution is found, return an empty list
    return []

# Example usage:
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Output: [0, 1]

