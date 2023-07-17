'''
Напишіть програму, що видаляє область дужок в стрічці:
["example (.com)", "github (.com)", "stackoverflow (.com)"] ->
example
github
stackoverflow
'''
import re

list1 = ["example (.com)", "github (.com)", "stackoverflow (.com)"]

list2 = [re.sub(r" \(.*\)", "", website) for website in list1]

print(list2)
