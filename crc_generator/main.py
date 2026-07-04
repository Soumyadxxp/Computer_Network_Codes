def findXor(a, b):
    n = len(b)
    result = ""
    for i in range(1, n):  # Skip first bit
        if a[i] == b[i]:
            result += '0'
        else:
            result += '1'
    return result


def mod2div(dividend, divisor):
    pick = len(divisor)
    tmp = dividend[0:pick]

    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = findXor(divisor, tmp) + dividend[pick]
        else:
            tmp = findXor('0' * pick, tmp) + dividend[pick]
        pick += 1

    if tmp[0] == '1':
        tmp = findXor(divisor, tmp)
    else:
        tmp = findXor('0' * pick, tmp)

    return tmp


def encodeData(data, key):
    n = len(key)

    # Append zeros
    padded_data = data + '0' * (n - 1)

    remainder = mod2div(padded_data, key)

    # Codeword
    codeword = data + remainder
    return codeword


if __name__ == "__main__":
    data = input(" Message (binary): ")
    key = input(" Generator (binary): ")   

    code = encodeData(data, key)

    print("\nGenerated Codeword:", code)