x=600851475143
for i in range(2,x):
    if x%i == 0:
        for y in range(2,i):
            if i%y !=0:
                print("prime factor:",i)
                break
    else:
        break    