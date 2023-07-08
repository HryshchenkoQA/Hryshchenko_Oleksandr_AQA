'''
2.Створіть словник із даними про студентів: ключі - імена студентів, значення - бали для кожного.
Програма повинна визначити середній бал і вивести імена студентів, чий бал вище середнього.
'''
# students = {"Alex": 85, "Petya": 92, "Vasya": 78, "Katya": 90, "Lera": 88, 'Masha': 50, "Leonid": 10}
# a_score = sum(students.values()) / len(students)
# above_average_students = [name for name, score in students.items() if score > a_score]
# print("Студенти з балом вище середнього:")
# for student in above_average_students:
#     print(student)
def find_students_above_average(scores):
    total_students = len(scores)
    total_score = sum(scores.values())
    average_score = total_score / total_students

    above_average_students = [name for name, score in scores.items() if score > average_score]

    return above_average_students


student_scores = {"Alex": 85, "Petya": 92, "Vasya": 78, "Katya": 90, "Lera": 88, 'Masha': 50, "Leonid": 10    }
above_average_students = find_students_above_average(student_scores)

print("Студенти з балами вище середнього:")
for student in above_average_students:
    print(student)

