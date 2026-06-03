# A function is a group of statement performing a specific task..
def avg():
    a = int(input("Enter First Number :"))
    b = int(input("Enter second Number :"))
    c = int (input("Enter third Number :"))
    average = (a + b+ c) / 3
    print(average)

# avg();

def goodDay(name):
    print(" Good Morning " + "" + name)
# goodDay("Ajay")

def factorial(n):
    if(n==0 or n==1):
        return 1
    return n * factorial(n-1)
n = int(input("Enter a Number :"))
print(f'The Factorial of number {factorial(n)}')