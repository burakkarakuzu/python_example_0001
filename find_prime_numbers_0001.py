while True:
    number1=int(input("Enter a number:"))
    if number1==1:
        break
    for i in range(2,number1):
        if number1%i==0:
            print("not prime number")
            break
        else:
            print("prime number:\n",number1)
            break
    print("-------------------------------\n")
    