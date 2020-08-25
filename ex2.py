x = int(input("Nhap x :"))
y = int(input("Nhap y :"))
tmp_y = y
count = 0
while x < y:
    if y % 2 == 0:
        y = y / 2
    else:
        y = y + 1
    count += 1
while y < x:
    y += 1
    count += 1
print("Result = ", count)
