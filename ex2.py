x = 7
y = 20
if y % 2 == 1:
    count = 1
    while x * 2 < y:
        x = x * 2
        count += 1
        print(f'operator {count}: x={x}, y={y}')
    left_bound = int(y / 2) + 1
    while x > left_bound:
        x = x - 1
        count += 1
        print(f'operator {count}: x={x}, y={y}')
    x = x * 2
    count += 1
    while True:
        if x == y:
            break
        x -= 1
        count += 1
        print(f'operator {count}: x={x}, y={y}')
else:
    count = 1
    while True:
        if x * 2 < y:
            x = x * 2
            count += 1
            print(f'operator {count}: x={x}, y={y}')
        elif x * 2 > y:
            x = x - 1
            count += 1
            print(f'operator {count}: x={x}, y={y}')
        elif x * 2 == y:
            x = y
            count += 1
            print(f'operator {count}: x={x}, y={y}')
            break
        if x == y:
            break
print("So buoc nho nhat de x = y la : ", count)