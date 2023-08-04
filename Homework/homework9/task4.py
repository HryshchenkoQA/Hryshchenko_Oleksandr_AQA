import random

numbers = [random.randint(1, 10) for i in range(100)]

counts = {}
for number in numbers:
    if number in counts:
        counts[number] += 1
    else:
        counts[number] = 1

for number, count in counts.items():
    print(number, count)

print(numbers)