import random

random_list = []

for i in range(5):
    random_list.append(random.randint(1, 100))

def bubblesort(random_list):
    for i in range(len(random_list) - 1):
        for j in range(len(random_list) - 1):
            print "Is {} > {}? {}".format(random_list[j], random_list[j + 1], random_list[j] >random_list[j + 1])
            if random_list[j] >= random_list[j + 1]:
                print "Switch\n"
                random_list[j], random_list[j + 1] = random_list[j + 1], random_list[j]
                print "Array after switching" ,random_list
                print
            else:
                print "Dont switch\n"
        print "{} after {} iteration".format(random_list, i + 1)
        print "End of run {}\n".format(i + 1)
        print "*********************************************************"


print "Initial array is",random_list
print "\n"

bubblesort(random_list)