s = input("Enter string: ")
l = []
for i in s:
    if i not in l:
        l.append(i)
for i in l:
    #print("{}{}".format(i, s.count(i)), end='')
    print(f'{i}{s.count(i)}', end='')
    