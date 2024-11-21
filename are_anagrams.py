def are_anagrams(str1, str2):
    """
    This function checks if two strings are anagrams of each other.

    Parameters:
    ----------
    str1 : str
        The first string to be compared.
    str2 : str
        The second string to be compared.

    Returns:
    -------
    bool:
        Returns True if the two strings are anagrams, otherwise False.

    Example:
    --------
    are_anagrams("listen", "silent")  # Output: True
    are_anagrams("hello", "world")    # Output: False
    """

    # Function implementation here ...
    output = False

    if len(str1) != len(str2):
        output = False 
    else:
        str1 = str1.lower()
        str2 = str2.lower()

        sorted_str1 = ''.join(sorted(str1))
        sorted_str2 = ''.join(sorted(str2))

        if sorted_str1 == sorted_str2:
            output = True

    return output

## Example 
# print(are_anagrams("listen", "silent"))  # Expected output: True
# print(are_anagrams("hello", "world"))    # Expected output: False

print(are_anagrams("lisen", "silent"))
print(are_anagrams("hello", "world"))
print(are_anagrams("act", "cat"))
