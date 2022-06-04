import re
fname = input('Enter file name: ')

if len(fname) < 1 :
    fname = 'Data.txt'

file = open(fname)
num_list = []

for line in file:
    line = line.rstrip()
    num = re.findall('([0-9]+)', line)
    if len(num) < 1 : continue
    
    for n in num:
        num_list.append(int(n))

print(sum(num_list))