def factorial():
    fact = 1
    numm = int(input("Enter a number "))
    for n in range(1,numm+1):
        fact *= n
    return fact

print(factorial())