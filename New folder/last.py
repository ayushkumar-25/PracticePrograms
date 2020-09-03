def mutate_string(string, i, c):
    string = s
    l = list(string)
    l[i] = c
    string ="".join(l)
    print (string)
    return("")

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
