def generateGamma(y0, y1, y2, len):
    y = [y0, y1, y2]
    for i in range(3, len + 1):
        yi = (y[i - 1] + y[i - 3]) % len
        y.append(yi)

    z = []
    for i in range(len):
        zi = (y[i] + y[i + 1]) % len
        z.append(zi)

    return z


def encrypt(text, n):
    result = []
    gamma = generateGamma(4,31,15, n)

    for i in range(len(text)):
        char = text[i]
        result.append((ord(char) + gamma[i] - 1040) % n)

    return result

def decrypt(text, n):
    result = ""
    gamma = generateGamma(4, 31, 15, n)

    for i in range(len(text)):
        char = text[i]
        result += chr((char  + (n - gamma[i])) % n + 1040)

    return result

encrypted = encrypt("ПРИКАЗЫВАЮФНАСТУПАТЬ", 32)
decrypted = decrypt(encrypted, 32)

print(encrypted)
print(decrypted)