 # リスト

# 合計値
def sum():
    sum_number = 0

    for r in range(0, len(numbers)):
        number = int(numbers[r])
        sum_number += number
    return sum_number


# 最大値
def max():
    max_number = 0

    for r in range(0, len(numbers)):
        num = int(numbers[r])
        if num > max_number:
            max_number = num
    return max_number


# 最小値
def min():
    min_number = numbers[0]
    for r in range(0, len(numbers)):
        if numbers[r] > numbers[r]:
            min_number = r
    return min_number


# 平均値
def average():
    average_number = int(sum() / len(numbers))
    return average_number


if __name__ == "__main__":
    numbers = input(("データを入力してください(スペース区切り) > ")).split()
    # split()で区切り文字で分割。

    print(f"合計値: {sum()}")
    print(f"最小値: {min()}")
    print(f"最大値: {max()}")
    print(f"平均値: {average()}") 

