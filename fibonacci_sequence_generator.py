terms = int(raw_input("How many Fibonnaci numbers to generate: "))
fib_list = [1, 1]
fib_list2 = []


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

''' Another way to generate fibonacci sequence'''

def fibonacci2(terms):
    if terms == 0:
        return 0
    elif terms == 1:
        return 1
    else:
        result = fibonacci2(terms - 1) + fibonacci2(terms - 2)
        return result

i = 1
while i <= terms:
    result = fibonacci2(i)
    fib_list2.append(result)
    i += 1

print fib_list2
