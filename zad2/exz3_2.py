def polindr(word):
    return word == word[::-1]


vvod = input("введите слово: ")
print("это слово полиндром: ", polindr(vvod))
