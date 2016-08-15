terms = int(raw_input("Find nth Fibonacci term: "))

def fibonacci(terms):
    if terms == 0:
        return 0
    elif terms == 1:
        return 1
    else:
        result = fibonacci(terms - 1) + fibonacci(terms - 2)
        return result

print fibonacci(terms)
