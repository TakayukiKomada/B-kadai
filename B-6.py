import random

dice_face = int(input("サイコロの面の数は?:"))
dice_challenge = int(input("何回振りますか?:"))
number = list()
for i in range(0, dice_challenge):
    n = random.randint(1, dice_face)
    number.append(n)
print(number)

print()
""" 末尾に要素を追加: append()
リストのメソッドappend()で、末尾（最後）に要素を追加できる。先頭など、末尾以外の位置に追加したい場合は後述のinsert()を使う """
