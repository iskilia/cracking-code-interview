def number_swapper(num1: int, num2: int):
    num1 = num1 - num2
    num2 = num1 + num2
    num1 = num2 - num1
    return num1, num2


if __name__ == "__main__":
    a = 1
    b = 2
    print(number_swapper(a,b))
