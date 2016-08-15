choice = True
cust_list = []
while choice:
    choice = raw_input("Enter Customer (Yes/No): ")
    choice = choice.lower()
    if choice == "no" or choice == "n":
        choice = False
        continue

    elif choice == "yes" or choice == "y":
        fname, lname = raw_input("Enter Customer name: ").split()
        cust_list.append({"fname": fname, "lname": lname})

    else:
        print "Invalid choice, please enter Yes/No"

for each in cust_list:
    print each['fname'], each['lname']