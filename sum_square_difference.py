def sumSquare1(n):
    return n*(n+1)*(2*n+1)/6
def sumSquare2(m):
    return (m*(m+1)/2)*(m*(m+1)/2)

num1=sumSquare1(100)
print("num1:",int(num1),"\n")
num2=sumSquare2(100)
print("num2:",int(num2),"\n")
print("num2-num1:",int(num2-num1))