print("Welcome to State bank of India")
a=int(input("Enter your 4 digit pin number: "))
b=25000
if(a==1234):
    print("1-Withdraw")
    print("2-Balance Enquiry")
    print("3-Fast Cash")
    c = int(input("Please choose transactions: "))
    if (c == 1):
        d=int(input("Enter withdraw amount: "))
        if (d < b and d%100 == 0):
            print("Please take your amount:", d)
        else:
            print("Invalid cash")

    elif(c==2):
        print("Your available amount : ",b)

    elif (c == 3):
        print("1->5,000")
        print("2->10,000")
        print("3->15,000")
        print("4->20,000")
        e = int(input("Enter fast cash option: "))
        if(e == 1 and 5000 < b):
            print("please take cash 5000")
        elif(e == 2 and 10000 < b):
            print("please take cash 10000")
        elif(e == 3 and 15000 < b):
            print("please take cash 15000")
        elif(e == 4 and 20000 < b):
            print("please take cash 20000")
        else:
            print("Invalid fast cash option")
else:
    print("Wrong pin number")
