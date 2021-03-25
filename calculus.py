import math
while True:
  while True:
    try:
      n1=float(input('Input Number 1'))
    except ValueError:
      print("Please, enter a valid number")
    break
  while True:
    operation=input('Input operation')
    if operation != "+" and operation !="-" and operation != "*" and operation != "/" and operation !="**" and operation != "square root":
      print ("Invalid operation name, dummy! Valid operation names are: [+], [-], [*], [/], [**] and [square root]! Please, correct your input below:")
    else:
      break
  while True:
    try:
      n2=float(input('Input Number 1'))
    except ValueError:
      print("Please, enter a valid number")
    break
  if operation == '+':
    print(n1+n2)
  elif operation == "-":
    print(n1-n2)
  elif operation == "*":
    print(n1*n2)
  elif operation == "/":
    print(n1/n2)
  #Power and Square Root DLC:
  elif operation == "**":
    print(n1**n2)
  elif operation == "square root":
    print(math.sqrt(n1))
    print(math.sqrt(n2))