import random
import urllib2
from itertools import islice

class EuroMillions:

    def __init__(self):
        pass

    def generate(self):
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

    def ten_frequent_numbers(self):
	url = 'https://www.national-lottery.co.uk/results/euromillions/draw-history/csv'
	response = urllib2.urlopen(url)
	html = response.read()

	with open('./euromillions_data.csv', 'wb') as f:f.write(html)
	euromillions_balls_dict = {}
	euromillions_stars_dict = {}
	master_balls_list = []
	master_stars_list = []
	concordance_balls_dict = {}
	concordance_stars_dict = {}
	with open('./euromillions_data.csv', 'r') as fh:
            for line in islice(fh, 1, None):
                tmp = line.split(',', 8)
                tmp = tmp[:8]
                euromillions_balls_dict[tmp[0]] = tmp[1:6]
                euromillions_stars_dict[tmp[0]] = tmp[-2:]
                

	for l in euromillions_balls_dict.values():
            master_balls_list.extend(l)

	for l in euromillions_stars_dict.values():
    	    master_stars_list.extend(l)

	for i in master_balls_list:
            concordance_balls_dict.setdefault(i, 0)
            concordance_balls_dict[i] = concordance_balls_dict[i] + 1

	for i in master_stars_list:
            concordance_stars_dict.setdefault(i, 0)
            concordance_stars_dict[i] = concordance_stars_dict[i] + 1

	print 'The top 10 most frequent balls in last 6 months euromillions draw are:'
	for key in sorted(concordance_balls_dict, key = concordance_balls_dict.__getitem__, reverse = True)[:10]:
            print '{0} -> {1} times'.format(key, concordance_balls_dict[key])

	print '\n\nThe top 10 most frequent lucky stars in last 6 months euromillions draw are:'
	for key in sorted(concordance_stars_dict, key = concordance_stars_dict.__getitem__, reverse = True)[:10]:
            print '{0} -> {1} times'.format(key, concordance_stars_dict[key])


class Lotto:

    def __init__(self):
        pass

    def generate(self):
        numbers = []

        while len(numbers) != 6:
            n = random.randint(1, 59)
            if n not in numbers:
                numbers.append(n)
        return numbers

    def ten_frequent_numbers(self):
        url = 'https://www.national-lottery.co.uk/results/lotto/draw-history/csv'
        response = urllib2.urlopen(url)
        html = response.read()

        with open('./lotto_data.csv', 'wb') as fh:
            fh.write(html)
        lotto_balls_dict = {}
        master_balls_list = []
	concordance_balls_dict = {}
	evenodd_balls_dict = {'Even': 0, 'Odd': 0}
	with open('./lotto_data.csv', 'r') as fh:
            for line in islice(fh, 1, None):
                tmp = line.split(',', 8)
                tmp = tmp[:8]
                lotto_balls_dict[tmp[0]] = tmp[1:7]                

	for l in lotto_balls_dict.values():
            master_balls_list.extend(l)
    
	for i in master_balls_list:
    	    concordance_balls_dict.setdefault(i, 0)
    	    concordance_balls_dict[i] = concordance_balls_dict[i] + 1
    	    if int(i) % 2 == 0:
                evenodd_balls_dict['Even'] = evenodd_balls_dict['Even'] + 1
   	    else:
                evenodd_balls_dict['Odd'] = evenodd_balls_dict['Odd'] + 1

	print 'The frequency of all balls in last 6 months lotto draws are:'
	for key in sorted(concordance_balls_dict, key = concordance_balls_dict.__getitem__, reverse = True)[:10]:
            print '{0} -> {1} times'.format(key, concordance_balls_dict[key])
	print '';print '';
	print 'The frequency of Even/Odd balls in last 6 months lotto draws are:'
	for key in sorted(evenodd_balls_dict, key = evenodd_balls_dict.__getitem__, reverse = True)[:60]:
            print '{0} -> {1} times'.format(key, evenodd_balls_dict[key])


def main():
    keep_generating = True
    print '\n'
    print '1. Euromillions'
    print '2. Lotto'
    print '3. Quit'
    main_option = input('Your choice: ')

    while keep_generating and main_option!= 3:
        if main_option == 1:
            print '1. Generate new Euromillions numbers'
            print '2. View last 10 Euromillions draws'
            print '3. View top 10 frequent numbers'
            print '4. Back to main menu'
            sub_option = input('Your choice: ')

        if main_option == 2:
            print '1. Generate new Lotto numbers'
            print '2. View last 10 draws'
            print '3. View top 10 frequent numbers'
            print '4. Back to main menu'
            sub_option = input('Your choice: ')

        if main_option == 1 and sub_option == 1:
            eur = EuroMillions()
            n1, l1 = eur.generate()
            print '\nNumbers: {0}  Lucky Stars: {1}\n'.format(sorted(n1), sorted(l1))

        if main_option == 2 and sub_option == 1:
            lot = Lotto()
            n2 = lot.generate()
            print '\nNumbers: {0}\n'.format(sorted(n2))
	
	if main_option == 1 and sub_option == 3:
	   eur = EuroMillions()
	   eur.ten_frequent_numbers()

	if main_option == 2 and sub_option == 3:
	    lot = Lotto()
	    lot.ten_frequent_numbers()

        if sub_option ==4:
            keep_generating = False
            main()

if __name__ == '__main__':
    main()

