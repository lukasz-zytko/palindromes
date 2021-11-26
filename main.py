def czy_palindrom(wyraz):
    """
        Returns True if the argument is palindrome
        Arguments:
        string
    """
    wyr = wyraz.lower()
    back = str()
    for i in range(len(wyr)-1, -1, -1):
        back += wyr[i]
    return True if wyr == back else False

#the easiest way
#def if_pal(s):
#    return s[::-1] == s