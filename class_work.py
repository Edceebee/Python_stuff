def conversion(celsius):
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit


print("hello" + 2)
a_str = 'hello'
a_str[1] = "r"

print(a_str)
hello_str = "hello world";
print(hello_str[0:11:2])

hello_str = "hello world";
print(hello_str[3:-2])
hello_str = 'hello world'
print(hello_str[0::-1])


def my_fun(param):
    param = [1, 2, 3]
    param.append(4)
    return param


my_list = [1, 2, 3]
new_list = my_fun(my_list)
print(my_list, new_list)
