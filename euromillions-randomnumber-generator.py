import random

keep_generating = True

def euromillions_number_generator():
    numbers = []
    luckystars = []

    while len(numbers) != 6:
        n = random.randint(1, 50)
        if n not in numbers:
            numbers.append(n)

    while len(luckystars) != 2:
        l = random.randint(1, 11)
        if l not in luckystars:
            luckystars.append(l)

    return numbers, luckystars

while keep_generating:
    print '1. Generate Euromillion Random numbers'
    print '2. Quit'
    option = raw_input('Your option: ')

    if int(option) == 1:
        n, l = euromillions_number_generator()
        print '\nNumbers: {0}  Lucky Stars: {1}\n'.format(sorted(n), sorted(l))
    if int(option) == 2:
        keep_generating = False