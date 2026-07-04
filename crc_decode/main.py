def findXor(a, b):
    n = len(b)
    result = ""
    for i in range(1, n):  # Skip first bit
        if a[i] == b[i]:
            result += "0"
        else:
            result += "1"
    return result


def mod2div(dividend, divisor):
    divisor_len = len(divisor)
    pick = divisor_len
    tmp = dividend[0:pick]
    zeros = "0" * divisor_len

    while pick < len(dividend):
        if tmp[0] == "1":
            tmp = findXor(divisor, tmp) + dividend[pick]
        else:
            tmp = findXor(zeros, tmp) + dividend[pick]
        pick += 1

    if tmp[0] == "1":
        tmp = findXor(divisor, tmp)
    else:
        tmp = findXor(zeros, tmp)

    return tmp


def decodeData(data, key):
    remainder = mod2div(data, key)

    # Correct Check: If there is no '1' in remainder, it's all zeros -> No Error
    if "1" not in remainder:
        return 0  # 0 means NO ERROR
    else:
        return 1  # 1 means ERROR DETECTED


if __name__ == "__main__":
    code = input("Enter CRC Code: ")
    key = input("Generator (binary): ")

    print("\nerror:", decodeData(code, key))