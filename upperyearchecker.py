while True:
  try:
    x = int(input("Input a year: "))
    break
  except ValueError:
    print("this is not a number")

if x % 4 == 0:
    print("this is a leap year")