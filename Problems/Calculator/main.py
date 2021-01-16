a, b = float(input()), float(input())
op = input()


def div_by_zero():
    print("Division by 0!")


if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "/":
    if b == 0:
        div_by_zero()
    else:
        print(a / b)
elif op == "*":
    print(a * b)
elif op == "mod":
    if b == 0:
        div_by_zero()
    else:
        print(a % b)
elif op == "pow":
    print(a ** b)
elif op == "div":
    if b == 0:
        div_by_zero()
    else:
        print(a // b)
