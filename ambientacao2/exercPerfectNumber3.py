def verifyNumber(num):
    total = 0
    for i in range(1, num):
        if (num%i == 0):
            total = total + i
            print(total)

    if(total == num):

        print("Perfect number")
        return 1
    else:

        print("Not a perfect number")
        return 0

num = int(input("Digit an integer: "))
exitcode = verifyNumber(num)