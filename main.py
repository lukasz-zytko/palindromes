def czy_palindrom(wyraz):
    wyr = wyraz.lower()
    back = str()
    for i in range(len(wyr)-1, -1, -1):
        back += wyr[i]
    return True if wyr == back else False

print(czy_palindrom("MAm"))