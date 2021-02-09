def add(num1: float, num2: float) -> float:
    """ a function that adds two numbers, num1 plus num2"""
    # logic
    num3 = num1 + num2
    return num3


def subtract(num1: float, num2: float) -> float:
    """ a function that subtracts two numbers, num1 minus num2"""
    # logic
    num3 = num1 - num2
    return num3


def multiply(num1: float, num2: float) -> float:
    """ a function that multiplies two numbers, num1 times num2"""
    # logic
    num3 = num1 * num2
    return num3


def divide(num1: float, num2: float) -> float:
    """ a function that divides two numbers, num1 divide num2"""
    # logic
    num3 = num1 / num2
    return num3


def square_root(num1: float) -> float:
    """ a function that returns the square root of a number"""
    # logic
    num2 = num1 ** 0.05
    return num2


def square(num1: float) -> float:
    """ a function that returns the square of a number"""
    # logic
    num2 = num1 ** 2
    return num2


def main():
    x = 2
    y = 10
    z = add(x, y)
    # run if __name__ == '__main__':
    main()
    print(f" x + y: {x} +{y} = {z}")
    #
