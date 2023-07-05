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
