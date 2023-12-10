import pandas
get_info=input()


fails = pandas.read_excel('2LD/description1.xlsx' , sheet_name='LookupAREA')
info_list = fails.values.tolist()

for x in range(len(info_list)):
    i=info_list[x][1]
    if i==get_info:
        reg_name=info_list[x][0]
        break

region=[]

with open('2LD/data.csv', 'r') as f:
    next(f)
    for line in f:
        row=line.rstrip().split(',')
        try:
            if row[1]==reg_name:
                region.append(int(row[3]))
        except NameError:
            break

print(sum(region))
