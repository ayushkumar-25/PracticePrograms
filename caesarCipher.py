# Program 6.3 of Python Book Reema Thareja

s = "HelloWorld"
index = 0
while index < len(s):
    letter = s[index]
    print(chr(ord(letter) + 3), end=" ")
    index += 1
