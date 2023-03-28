num1 = 1
num2 = 0
while num1 >= num2:
    num1 = int(input("First variable: "))
    num2 = int(input("Second variable: "))
    if num1 < num2:
        print("first number is smaller than the second ", num1, " < ", num2, " closing program")
        break
