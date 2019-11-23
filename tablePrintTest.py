from tabulate import tabulate

rt_tbl_D = {'H1': {'RA': 1, 'RB': 2}, # {destination: {router: cost}}
            'H2': {'RA': 4, 'RB': 3}, 
            'RA': {'RA': 0, 'RB': 1}, 
            'RB': {'RA': 1, 'RB': 0}}
            
name = '*RA*'
headers = []
rowIDs = set()

for x in rt_tbl_D:
    headers.append(x)
    for y in rt_tbl_D[x]:
        rowIDs.add(y)

# table = rt_tbl_D
print(rt_tbl_D)

data = []

for m in headers:
    for n in rowIDs:
        data.append(rt_tbl_D[m][n])
    rt_tbl_D[m] = data
    data = []

headers = [name] + headers

print(rt_tbl_D)
print()

print(headers)
print(rowIDs)


print(tabulate(rt_tbl_D, headers, showindex=rowIDs, tablefmt="fancy_grid"))




# print(rt_tbl_D)
# table_width = len(rt_tbl_D) + 1
# print(table_width)
# key1 = list(rt_tbl_D)[0]
# table_height = len(rt_tbl_D[key1]) + 1
# print(table_height)
# name = 'RA'

# table_printer_string = '╒'

# for x in rt_tbl_D:
#     print(x)


