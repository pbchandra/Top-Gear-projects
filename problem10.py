def fun_args(*arg):
    a = arg[0]
    b = arg[1]
    c = a + b
    print("\n Addition of two numbers is", c)
    c = a - b
    print("\n Subtraction of two numbers is", c)
    c = a * b
    print("\n Multiplication of two numbers is", c)
    c = a / b
    print("\n Division of two numbers is", c)
    c = a % b
    print("\n modulus of two numbers is", c)
    c = a ** b
    print("\n Exponentiation of two numbers is", c)
    c = a // b
    print("\n Floor division of two numbers is", c)


fun_args(int(input("enter two numbers")), int(input()))
