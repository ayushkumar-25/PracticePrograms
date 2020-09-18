string = input()
count = string.count('-')
string = string.split('-')
print('-'*count + ''.join(string)) 