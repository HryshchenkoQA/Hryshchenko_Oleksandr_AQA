'''
Напишите функцию is_palindrome, которая принимает строку в качестве аргумента и возвращает True,
если строка является палиндромом (читается одинаково слева направо и справа налево), и False в противном случае.
'''

def is_palindrome():
    string = input("Введите строку: ")
    string = string.replace(" ", "").lower()
    return string == string[::-1]

print(is_palindrome())

