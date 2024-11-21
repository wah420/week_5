def sum_of_evens(min_value, max_value):
    
    """Find the sum of even numbers between two given numbers (inclusive).

    Args:
        min_value (int): Minimum number
        max_value (int): Maximum number

    Returns:
        total: sum of the even numbers between min_value and max_value

    Example:

    min_value = 10
    max_value = 13
    total = sum_of_evens(min_value, max_value)
    print(total) # total is 22.

    """



    # Function implementation here ...
    if min_value > max_value:
        return 0
    
    total = sum(num for num in range(min_value, max_value + 1) if num % 2 == 0)

    return total

# # # Run code example
# min_value = 10
# max_value = 13
# result = sum_of_evens(min_value, max_value) # returns 22

min_value = 8
max_value = 21
result = sum_of_evens(min_value, max_value)
print(result)