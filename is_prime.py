import math

def is_prime(num):
    """Checks if a number is prime.

    Input:
        num (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.

    Example:

    boolean = is_prime(5)   # returns True
    print(boolean)
    """
    
    output = True
    
    if num <= 1:
        output = False  
    elif num == 2:
        output = True  
    elif num % 2 == 0:
        output = False 
    else:
        for i in range(3, int(math.sqrt(num)) + 1, 2):
            if num % i == 0:
                output = False  
                break  
    
    return output

# Run code examples
boolean = is_prime(5)   
print(boolean)          

boolean = is_prime(12)  
print(boolean)          

boolean = is_prime(3)  
print(boolean)          
