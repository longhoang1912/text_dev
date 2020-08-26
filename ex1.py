data = '123456789'
index = 1
count = 0
list_result = []

while True:
    temp = []
    for data in list_result:
        if count + index >= len(data):
            continue
        sm = data[:index + count] + "+" + data[index + count:]
        sub = data[:index + count] + "-" + data[index + count:]
        non = data[:index + count] + "@" + data[index + count:]
        temp.append(sm)
        temp.append(sub)
        temp.append(non)
    list_result.extend(temp)
    temp = [data[:index] + "+" + data[index:],
            data[:index] + "-" + data[index:],
            data[:index] + "@" + data[index:]]
    list_result.extend(temp)
    index += 1
    count += 1
    if index == 9:
        break
    
list_result = set([i.replace("@", "") for i in list_result])
result = [num for num in list_result if eval(num) == 100]
print(result)