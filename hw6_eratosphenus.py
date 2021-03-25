x = int(input("Please, enter an int number"))
table = list(range(0,(x+1)))
print("Your list: ", table)

for x in table:
    for y in table:
        if x != y and x != 0 and y !=0:
            if y % x == 0:
              table.remove(y)

print("Your eratosphenus resheto: ", table)