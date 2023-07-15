'''
Напишіть програму яка перевіряє чи стрічка містить лише великі і малі літери, числа та нижнє підкреслення.
'''
import re
string1 = 'Hello there! Im GENERAL Kenobie'
pattern1 = re.compile(r'^[a-zA-Z0-9_]+$')
check1 = pattern1.match(string1)
print(check1)