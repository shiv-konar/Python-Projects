terms = int(raw_input("How many Fibonnaci numbers to generate: "))
fib_list = [1, 1]


def fibonacci(terms, firstnum = 1, secondnum = 1):
    if terms == 0:
        return []
    elif terms == 1:
        return [1]
    elif terms == 2:
        return [1,1]
    else:
        result = firstnum + secondnum
        fib_list.append(result)
        fibonacci(terms -1, secondnum, result)
    return fib_list

print fibonacci(terms)
