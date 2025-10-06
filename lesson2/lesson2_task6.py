lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
for a in range(0, len(lst)):
    if lst[a]%3 == 0 and lst[a]<30:
        print(lst[a])