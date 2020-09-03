a =[]
def swap_case(s):

    for i in s:
        if (i>='A' and i<='Z'):
            a.append(i.lower())
        elif (i>='a' and i<='z'):
            a.append(i.upper())
        else:
            a.append(i)
s = input()
swap_case(s)
print(a)
st = "".join(a)
print(st)

        




'''if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)'''
