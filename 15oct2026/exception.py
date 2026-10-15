try:
    a = input("enter the number 1:")
    b = input("enter the number 2:")
    print(int(a)/int(b))
except ValueError:
    print("give the number as a input")
except zeroDivisionError:
        print("cannot divide by zero")
