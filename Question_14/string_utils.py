# string_utils.py

def reverse_string(s: str) -> str:
    """
    Reverses the input string.

    Parameters:
    s (str): The string to be reversed.

    Returns:
    str: The reversed string.
    """
    return s[::-1]


def capitalize_string(s: str) -> str:
    """
    Capitalizes the first letter of each word in the input string.

    Parameters:
    s (str): The string to be capitalized.

    Returns:
    str: The string with the first letter of each word capitalized.
    """
    return s.title()
