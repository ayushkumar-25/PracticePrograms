#print (''.join([i.lower() if i.isupper() else i.upper() for i in input()]))

def swap_case(s):


    for i in s:
        if (i>='A' and i<='Z'):
            print(i.lower(),end="")
        if (i>='a' and i<='z'):
            print(i.upper(),end="")
        else:
            print(i,end="")

    return

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
