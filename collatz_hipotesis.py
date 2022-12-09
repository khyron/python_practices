number = int(input("ingrese numero:"))
steps = 0
while number != 1 :
    steps += 1
    if number % 2 == 0 :
        number = number / 2
        print(int(number))
    elif number % 2 == 1 :
        number = 3 * number + 1
        print(int(number))
print("steps:", int(steps))


