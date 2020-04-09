'''def case():
    c = input("Enter a letter: ")
    if (c >= 'A' and c<= 'Z'):
        print(c.lower())
    else:
        print(c.upper())

case()'''


N = int(input())
a = []
for i in range(N):
    a.append(input())
a.reverse()

print(''.join(a))
