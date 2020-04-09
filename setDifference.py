# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
for i in range(n):
    p = list(input())

    for i in range(9):
        if (p[i]>='0' or p[i]<='9'):

            if(p[0] == '7' or p[0] == '8' or p[0]=='9'):
                if (len(p)==10):
                    print("YES")
                else:
                    ("NO")
            else:
                print("NO")
        else:
            print("NO")
