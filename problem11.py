def fun_args(*arg):
    a = arg[0] and arg[1]
    b = arg[0] or arg[1]
    c = not (arg[0] and arg[1])
    print("\n", a, "\n", b, "\n", c, )


fun_args(int(input("enter three binary numbers",)), int(input()), int(input()))
