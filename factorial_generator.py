num = int(raw_input("Generate factorial for: "))


def factorial(num):
    if num <= 1:
        return 1
    else:
        fact = num * factorial(num - 1)
    return fact

print "{}! = {}".format(num, factorial(num))