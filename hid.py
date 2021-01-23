from time import sleep

keycodeMap = {
    " ": 0x2c,
    "0": 0x27,
    "`": 0x35,
    "-": 0x2d,
    "=": 0x2e,
    "[": 0x2f,
    "]": 0x30,
    "\\": 0x31,
    ";": 0x33,
    "'": 0x34,
    ",": 0x36,
    ".": 0x37,
    "/": 0x38,
}

shiftedKeyCodeMap = {
    "~": 0x35,
    "!": 0x1e,
    "@": 0x1f,
    "#": 0x20,
    "$": 0x21,
    "%": 0x22,
    "^": 0x23,
    "&": 0x24,
    "*": 0x25,
    "(": 0x26,
    ")": 0x27,

    "_": 0x2d,
    "+": 0x2e,
    "{": 0x2f,
    "}": 0x30,
    "|": 0x31,
    ":": 0x33,
    '"': 0x34,
    "<": 0x36,
    ">": 0x37,
    "?": 0x38,
}

CTRL, SHIFT, ALT, META = [1 << i for i in range(4)]
ENTER = 0x28

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

def sendKeys(*args):
    for arg in args:
        with open("/dev/hidg0", "wb+") as f:
            if isinstance(arg, str):
                for c in arg:
                    code, shifted = convert(c)
                    byteseq = bytes([2 if shifted else 0, 0, code, 0, 0, 0, 0, 0])
                    f.write(byteseq)
                    f.write(b"\x00" * 8)
            elif isinstance(arg, int):
                byteseq = bytes([0, 0, arg]).ljust(8, b"\x00")
                f.write(byteseq)
                f.write(b"\x00" * 8)


def sendCombo(*args):
    mod = 0
    keys = []
    for arg in args:
        if isinstance(arg, int):
            mod |= arg
        elif isinstance(arg, str):
            keys += [convert(c)[0] for c in arg]
    
    byteseq = bytes([mod, 0] + keys[:6]).ljust(8, b"\x00")
    
    with open("/dev/hidg0", "wb+") as f:
        f.write(byteseq)
        f.write(b"\x00" * 8)


sendCombo(META, "r")
sleep(1)
sendKeys("notepad", ENTER)
sleep(1)
sendKeys("Hello World! 012345: This is a tilde (~)")