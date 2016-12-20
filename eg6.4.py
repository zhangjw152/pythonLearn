begin = 0
while True:
    begin += 1
    if begin == 942:
        break
    elif begin % 3 == 0:
        continue
    else:
        print begin
