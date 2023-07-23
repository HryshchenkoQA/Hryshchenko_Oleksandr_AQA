def age_group(age):
  if age >="1" and age <="18":
    return "You're so young"
  elif age >="19" and age <= "35":
    return "You're a cool young guy, as Rayan Gosling"
  elif age >="36" and age <= "99":
    return "Nevermind, life is just begun"
  else:
    return "error"

#if __name__ == "__Task1_hw8__":
if __name__ == "__main__":
  age = input('Enter your age here: ')
  greeting = age_group(age)
  print(greeting)