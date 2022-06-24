x = int(input("行数を入力してください: "))
y = int(input("列数を入力してください: "))

for x in range(1, x+1):
    for y in range(1, y+1):
        print(x * y, end=" ")
    print()
