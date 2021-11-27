def if_palindrome(str):
    """
        Returns True if the argument is palindrome
        Arguments:
        string
    """
    return str[::-1] == str

print(if_palindrome("potop"))