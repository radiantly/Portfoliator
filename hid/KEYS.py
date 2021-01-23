CTRL, SHIFT, ALT, META = [1 << i for i in range(4)]
ENTER = 0x28

LEFT = 0x50
DOWN =  0x51
UP = 0x52
RIGHT = 0x4F

keycodeMap = {
    " ": 0x2C,
    "0": 0x27,
    "`": 0x35,
    "-": 0x2D,
    "=": 0x2E,
    "[": 0x2F,
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
    "!": 0x1E,
    "@": 0x1F,
    "#": 0x20,
    "$": 0x21,
    "%": 0x22,
    "^": 0x23,
    "&": 0x24,
    "*": 0x25,
    "(": 0x26,
    ")": 0x27,
    "_": 0x2D,
    "+": 0x2E,
    "{": 0x2F,
    "}": 0x30,
    "|": 0x31,
    ":": 0x33,
    '"': 0x34,
    "<": 0x36,
    ">": 0x37,
    "?": 0x38,
}
