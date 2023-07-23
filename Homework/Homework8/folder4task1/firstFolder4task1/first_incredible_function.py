def is_master(name):
  if name == "Alex":
    return "Hello, my Master"
  else:
    return "Possible you are not my Master, but welcome^_^"

  #if __name__ == "__Task1_hw8__":
if __name__ == "__main__":
  name = input("Hi, what is your name? Enter here, please: ")
  greeting = is_master(name)
  print(greeting)

