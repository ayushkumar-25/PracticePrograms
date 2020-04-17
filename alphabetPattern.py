# Program 6.1 of python book of Reema Thareja

for i in range(1, int(input())):
    ch = "A"
    for j in range(i):
        print(ch, end='')
        ch = chr(ord(ch) + 1)
    print()
