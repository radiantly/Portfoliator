from time import sleep

keycodeMap = {
    " ": 0x2c,
    "0": 0x27
}

shiftedKeyCodeMap = {
    "!": 0x1e
}

def convert(c):
    # Lower case letters
    if 97 <= ord(c) <= 122:
        return ord(c) - 93, False

    # Upper case letters
    if 65 <= ord(c) <= 90:
        return ord(c) - 61, True

    # Numbers
    if 49 <= ord(c) <= 57:
        return ord(c) - 49 + 0x1e, False
    
    if c in keycodeMap:
        return keycodeMap[c], False

    if c in shiftedKeyCodeMap:
        return shiftedKeyCodeMap[c], True

    return 0, False

def sendkeys(text):
    with open("/dev/hidg0", "wb+") as f:
        for c in text:
            code, shifted = convert(c)
            byteseq = bytes([2 if shifted else 0, 0, code, 0, 0, 0, 0, 0])
            f.write(byteseq)
            f.write(b"\x00" * 8)

sendkeys("Hello World! 012345")