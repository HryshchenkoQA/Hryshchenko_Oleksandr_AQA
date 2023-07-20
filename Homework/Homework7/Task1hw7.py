'''
Написати функцію, яка отримує у вигляді параметра ім'я файлу назви інтернет доменів (domains.txt)
та повертає їх у вигляді списку рядків (назви повертати без крапки).
'''

def get_domains():
    domains = []
    with open('txt_for_HW7/domains.txt', "r") as f:
        domains = f.read().splitlines()
    for domain in domains:
        domain = domain.strip(".")
        print(domain)

get_domains()