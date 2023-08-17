a = 10
b = 0

try:
    c = a/b
    print("the result is: ",c)

except ZeroDivisionError:
    print(f"{a} cannot be divided with zero")



except Exception as error:
    print("There is a error ")

print("============================")


