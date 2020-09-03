decimalNumber = int(input("Enter number in decimal: "))

#converting number to Binary, Octal & Hex
binaryNumber = bin(decimalNumber)
octalNumber = oct(decimalNumber)
hexNumber = hex(decimalNumber)

#printing the numbers
print("\n")
print("Binary of {} : {}".format(decimalNumber,binaryNumber))
print("Octal of {} : {}".format(decimalNumber,octalNumber))
print("Hexadecimal of {} : {}".format(decimalNumber,hexNumber))
