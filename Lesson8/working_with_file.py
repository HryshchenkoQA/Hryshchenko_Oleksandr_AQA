'''
file2 = open('a.txt', 'w')
file2.write('New line written by me')   #write полностью перезаписывает

file2.close()
'''


file1 = open('a.txt', 'r')
our_lines = file1.read()
print(our_lines)
file1.close()


file2 = open('a.txt', 'w')
file2.write('New line written by me\n')   #write полностью перезаписывает
file2.writelines(['first line\n', 'second line\n'])    #.writelines добавляет

file2.close()

file3 = open('a.txt', 'a')
file3.write('this is third line of text')    #file_name +'a', .write  - добавляет текст с новой строки
file3.close()

permanent_lines = []
with open('a.txt', 'r') as a:
    permanent_lines= a.readlines()
    print(permanent_lines)

with open('a.txt', 'w') as a:
    for line in permanent_lines:
        if len(line) < 20:
            permanent_lines[permanent_lines.index(line)] = "We changed this\n"
    a.writelines(permanent_lines)

