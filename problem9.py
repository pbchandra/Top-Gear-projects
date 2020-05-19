def fun_args(*arg):
    a = complex(arg[0], arg[1])
    b = complex(arg[2], arg[3])
    c = a + b
    print("\n Addition of two numbers is", c)
    c = a - b
    print("\n Subtraction of two numbers is", c)
    c = a * b
    print("\n Multiplication of two numbers is", c)
    c = a / b
    print("\n Division of two numbers is", c)


fun_args(int(input()), int(input()),int(input()), int(input()))
