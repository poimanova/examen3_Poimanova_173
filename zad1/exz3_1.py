def card_nom(card):
    return '*' * len(card[:-4]) + card[-4:]
num = input("введите номер карты: ")

print(card_nom(num))


