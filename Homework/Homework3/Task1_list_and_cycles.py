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
    note = input("Введіть нотатку: ")
    notes.append(note)
    print("Нотатка додана.")


def view_notes(order):
    if order == "earliest":
        sorted_notes = list(notes)
    elif order == "latest":
        sorted_notes = list(reversed(notes))
    elif order == "longest":
        sorted_notes = sorted(notes, key=len, reverse=True)
    elif order == "shortest":
        sorted_notes = sorted(notes, key=len)
    else:
        print("Неправильний вибір. Будь ласка, спробуйте ще раз.")
        return

    print(f"Від {order} до най{'пізнішої' if order in ['earliest', 'latest'] else 'коротшої'}:")
    for note in sorted_notes:
        print(note)


while True:
    action = input("Введіть команду (add, earliest, latest, longest, shortest, Exit): ")

    if action == "add":
        add_note()
    elif action == "earliest":
        view_notes("earliest")
    elif action == "latest":
        view_notes("latest")
    elif action == "longest":
        view_notes("longest")
    elif action == "shortest":
        view_notes("shortest")
    elif action == "Exit":
        break
    else:
        print("Неправильна команда. Будь ласка, спробуйте ще раз.")

print("Програма завершила роботу.")
