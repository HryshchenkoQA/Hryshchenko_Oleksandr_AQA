def choice(cinema):
  if cinema == "oppenheimer" or cinema =="Oppenheimer":
    return "Nolan is a genius"
  elif cinema == 'barbie' or cinema == "Barbie":
    return "Literally me, im DRIVE with Harley Quinn"
  elif cinema == "both" or cinema == "Both":
    return "You're god damm right"
  else:
    return "Error"

#if __name__ == "__Task1_hw8__":
if __name__ == "__main__":
  cinema = input("Barbie or Oppenheimer? Or maybe both of them?): ")
  answer = choice(cinema)
  print(answer)


