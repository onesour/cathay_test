def count_letter(sentence: str) -> dict:
    result = {}
    for s in sentence:
        if s == " ":
            continue
        if 122 >= ord(s) >= 97:
            s = chr(ord(s) - 32)
        if s in result.keys():
            result[s] += 1
        else:
            result[s] = 1
    return result


if __name__ == "__main__":
    input_sentence = "Hello welcome to Cathay 60th year anniversary"
    count_result = count_letter(input_sentence)
    for key in sorted(count_result.keys()):
        print(f"{key}: {count_result[key]}")