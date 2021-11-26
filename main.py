def czy_palindrom(wyraz):
    back = str()
    for i in range(len(wyraz)-1, -1, -1):
        back += wyraz[i]
    if wyraz == back:
        return True
    else:
        return False

check = czy_palindrom("nie kajak")
print(check)