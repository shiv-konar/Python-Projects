antonym = raw_input("Enter antonym: ")

antonym_list = antonym.split()

acronym = ""

for each in antonym_list:
    acronym += each[0].capitalize()

print "Acronym of {} is {}".format(antonym, acronym)
