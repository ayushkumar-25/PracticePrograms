n = input()

for i in n:
    if (i>='A' and i<='Z'):
        print(i.lower(),end="")
    if (i>='a' and i<='z'):
        print(i.upper(),end="")
    else:
        print(i,end="")




'''a =n.split(" ")
print(a)
print("".join(a))
'''

'''def split_and_join(lin):
    a = line.split(" ")
    return "-".join(a)
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)'''


