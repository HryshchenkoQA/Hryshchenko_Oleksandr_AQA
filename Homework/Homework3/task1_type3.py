'''
Написати програму, для введення та перегляду нотаток. Програма пропонує користувачу вводити ключові слова,
та опрацьовує їх. Перелік ключових слів:

add - додати нотатку. Користувач вводить текст нотатки, який зберігається у програмі та є дійсним до її завершення
earliest - виводить збережені нотатки у хронологічному порядку - від найстарішої до найновішої
latest - виводить збережені нотатки у хронологічному порядку - від найновішої до найстарішої
longest - виводить збережені нотатки у порядку їх довжини - від найдовшої до найкоротшої
shortest - виводить збережені нотатки у порядку їх довжини - від найкоротшої до найдовшої
Exit - вихід
'''

notes = []
def add_note():
    note = input('Add note here: ')
    notes.append(note)
    print("Note was added.")

def view(sort):
    if sort == "earliest":
        sort_notes =list(notes)
    elif sort == "latest":
        sort_notes =list(reversed(notes))
    elif sort == "longest":
        sort_notes =sorted(notes, key=len, reverse=True)
    elif sort == "shortest":
        sort_notes =sorted(notes, key=len)
    else:
        print("Error choice, try again")
        return
    for note in sort_notes:
        print(note)

while True:
    action =input("Enter the command: (add, earliest, latest, longest, shortest or exit): ")
    if action == "add":
        add_note()
    elif action == "earliest":
        print("From earliest to latest")
        view('earliest')

    elif action == "latest":
        print("From latest to earliest")
        view("latest")

    elif action == "longest":
        print("From longest to shortest")
        view('longest')

    elif action == "shortest":
        print("From shortest to longest")
        view('shortest')

    elif action == "exit":
        break
    else:
        print("Error command, try again")
print("Good bye")







