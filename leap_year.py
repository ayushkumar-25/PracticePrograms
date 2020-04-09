def year():

    
    if (y%4==0):
        if (y%100==0):
            if (y%400==0):
                print("Leap year")
            else:
                print("Not a Leap year.")
        else:
            print('Leap year.')
    else:
        print('Not a Leap year')

for i in range (0,5):
    y = int(input("\nEnter the year: "))
    year()


