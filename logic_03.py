def count_last_member(people: int) -> int:
    all_member_index = [True] * people
    index = 0
    count = 0
    while sum(all_member_index) > 1:
        if index == len(all_member_index):
            index = 0
        if all_member_index[index] is True:
            # If this person still in group, say number.
            count += 1
        if count % 3 == 0:
            count = 0
            all_member_index[index] = False
        index += 1
    last_member = all_member_index.index(True) + 1
    return last_member


if __name__ == "__main__":
    n = int(input("請輸入人數："))
    result = count_last_member(n)
    print(f"最後剩下的人為原先的第 {result} 位")
