print("\n STAR EVENTS PRESENTS YOU ")
n1 = input("\n PLEASE ENTER YOUR NAME: ")
ph = int(input("\n PLEASE ENTER YOUR MOBILE NUMBER: "))

print("\n LIST OF EVENTS :\n 1.BIRTHDAY PARTY \n 2.WEDDING ANNIVERSARY \n 3.MARRIAGE EVENT \n")
op1 = int(input("PLEASE SELECT AN EVENT YOU ARE LOOKING FOR: "))
if op1 == 1:
    print("\n YOU HAVE SELECTED BIRTHDAY PARTY ")
    print("\n THE DECORATIONS WE PRESENT FOR YOU :\n 1.BALLOON DECORATION \n 2.FLOWER DECORATION \n 3.LIGHTINGS ")
    op2 = int(input("\n SELECT THE DECORATION YOU LIKE: "))

    if op2 == 1:
        bill1 = 10000
        print("\n YOU HAVE SELECTED BALLOON DECORATION\n YOUR DECORATION BILL:", bill1)
    elif op2 == 2:
        bill1 = 20000
        print("\n YOU HAVE SELECTED FLOWER DECORATION\n YOUR DECORATION BILL:", bill1)
    else:
        bill1 = 30000
        print("\n YOU HAVE SELECTED LIGHTINGS\n YOUR DECORATION BILL:", bill1)

elif op1 == 2:
    print("\n YOU HAVE SELECTED WEDDING ANNIVERSARY")
    print("\n THE DECORATIONS WE PRESENT FOR YOU :\n 1.BALLOON DECORATION \n 2.FLOWER DECORATION \n 3.LIGHTINGS ")
    op2 = int(input("\n SELECT THE DECORATION YOU LIKE: "))

    if op2 == 1:
        bill1 = 20000
        print("\n YOU HAVE SELECTED BALLOON DECORATION\n YOUR DECORATION BILL:", bill1)
    elif op2 == 2:
        bill1 = 30000
        print("\n YOU HAVE SELECTED FLOWER DECORATION\n YOUR DECORATION BILL:", bill1)
    else:
        bill1 = 40000
        print("\n YOU HAVE SELECTED LIGHTINGS\n YOUR DECORATION BILL:", bill1)

else:
    print("\n YOU HAVE SELECTED MARRIAGE EVENT")
    print("\n THE DECORATIONS WE PRESENT FOR YOU :\n 1.BALLOON DECORATION \n 2.FLOWER DECORATION \n 3.LIGHTINGS ")
    op2 = int(input("\n SELECT THE DECORATION YOU LIKE: "))

    if op2 == 1:
        bill1 = 300000
        print("\n YOU HAVE SELECTED BALLOON DECORATION\n YOUR DECORATION BILL:", bill1)
    elif op2 == 2:
        bill1 = 400000
        print("\n YOU HAVE SELECTED FLOWER DECORATION\n YOUR DECORATION BILL:", bill1)
    else:
        bill1 = 500000
        print("\n YOU HAVE SELECTED LIGHTINGS\n YOUR DECORATION BILL:", bill1)

op3 = int(input("\n WOULD YOU LIKE TO ORDER A CAKE: \n 1.YES \n 2.NO\n"))

if op3 == 1:
    print("\n FLAVORS WOULD YOU LIKE TO SELECT:\n 1.VANILLA\n 2.STRAWBERRY\n 3.CHOCOLATE\n")
    op3 = int(input("\n SELECT YOUR OPTION: "))

    if op3 == 1:
        bill2 = 2000
        print("\n YOU HAVE SELECTED VANILLA FLAVOR\n BILL:", bill2)
        bill = bill1 + bill2
        print("\n TOTAL BILL:", bill)
    elif op3 == 2:
        bill2 = 3000
        print("\n YOU HAVE SELECTED STRAWBERRY FLAVOR\n BILL:", bill2)
        bill = bill1 + bill2
        print("\n TOTAL BILL:", bill)
    else:
        bill2 = 4000
        print("\n YOU HAVE SELECTED CHOCOLATE FLAVOR\n BILL:", bill2)
        bill = bill1 + bill2
        print("\n TOTAL BILL:", bill)
else:
    bill = bill1
    print("\n TOTAL BILL:", bill)

print("\n THANK YOU", n1, "FOR CHOOSING OUR STAR EVENTS...")
print(" CONFIRMATION MESSAGE WILL BE SENT TO", ph)
print(" AND WE WILL CONFIRM YOUR ADDRESS")
print(" WE HOPE WE MAKE YOUR EVENT GRAND SUCCESS")
print("\n FOR ANY FURTHER REQUIREMENTS PLEASE CONTACT OUR MANAGER 9080706756")