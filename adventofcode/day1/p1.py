with open('input.txt', 'r') as file:
    data = file.read().splitlines()


current = 50
count = 0
for line in data:
    direction = -1 if line[0] == 'L' else 1
    value = int(line[1:])
    for i in range(value):
        current += direction
       
        current %= 100
        if current == 0:
            count += 1

print(count)