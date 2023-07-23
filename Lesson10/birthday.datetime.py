import datetime


birthday = input("Введите дату своего дня рождения (YYYY-MM-DD): ")
today = datetime.date.today()
days_until_birthday = (today - datetime.date.fromisoformat(birthday)).days
print(f"До вашего дня рождения осталось {days_until_birthday} дней.")
