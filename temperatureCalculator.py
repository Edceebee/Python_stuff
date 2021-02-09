from utils import add, multiply


def convert(celsius):
    fahrenheit = multiply(celsius, 1.8)
    return add(fahrenheit, 32)


celsius = input("Enter multiple values separated by coma  :")
celsius_values = celsius.split()

for celsius in celsius_values:
    celsius = float(celsius)
    fahrenheit = convert(celsius)

    print("the fahrenheit of", celsius, "is", fahrenheit)



