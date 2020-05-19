def fun_args(*args):
    print("First number is", args[0])
    print("Second number is", args[1])
    print("Third number is", args[2])
    print("The biggest of three numbers is", max(args[0], args[2], args[1]))


fun_args(input(), input(), input())
