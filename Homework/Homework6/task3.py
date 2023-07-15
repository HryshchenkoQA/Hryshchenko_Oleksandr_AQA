'''
Напишіть програму, що. вставляє пробіл перед великою літерою
'''
import re
string1 = "hi, my name is generalKenobi"
insert_space = re.sub(r"([A-Z])", r" \1", string1)
print(insert_space)
