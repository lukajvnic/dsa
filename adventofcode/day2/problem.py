

with open("input.txt", 'r') as file:
    data = file.read().split(',')


total = 0
for id_range in data:
    start, end = map(int, id_range.split('-'))
    for item_id in range(start, end + 1):
        str_id = str(item_id)
        good = False
        for sizerange in range(1, len(str_id)//2 + 1):
            if str_id.count(str_id[0:sizerange]) * str_id[0:sizerange] == str_id:
                good = True
                break
        if good:
            total += item_id

print(total)
