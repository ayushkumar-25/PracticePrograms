#capitals = {"India":"Delhi", "USA":"New York", "Japan":"Tokoyo"}
#for i in capitals.keys():
  #print("The capital of {} is {} ".format(i,capitals.get(i)))


#prime number code
num = int(input("Enter a number: "))
for i in range (2,num):
    if num%i ==0:
        print("The number is not a prime number")
        break
else:
    print("Prime!")
