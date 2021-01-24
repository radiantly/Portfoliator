from time import sleep

from hid.KEYS import keycodeMap, shiftedKeyCodeMap


class Keyboard:
    def __init__(self):
        self.typeDelay = 0.1
        self.execDelay = 0.5

    def convert(self, c):
        # Lower case letters
        if 97 <= ord(c) <= 122:
            return ord(c) - 93, False

        # Upper case letters
        if 65 <= ord(c) <= 90:
            return ord(c) - 61, True

        # Numbers
        if 49 <= ord(c) <= 57:
            return ord(c) - 49 + 0x1E, False

        if c in keycodeMap:
            return keycodeMap[c], False

        if c in shiftedKeyCodeMap:
            return shiftedKeyCodeMap[c], True

        return 0, False

    def sendKeys(self, *args):
        for arg in args:
            with open("/dev/hidg0", "wb+") as f:
                if isinstance(arg, str):
                    for c in arg:
                        code, shifted = self.convert(c)
                        byteseq = bytes([2 if shifted else 0, 0, code, 0, 0, 0, 0, 0])
                        f.write(byteseq)
                        f.write(b"\x00" * 8)
                elif isinstance(arg, int):
                    byteseq = bytes([0, 0, arg]).ljust(8, b"\x00")
                    f.write(byteseq)
                    f.write(b"\x00" * 8)
        sleep(self.execDelay)

    def typeKeys(self, *args, **kwargs):
        """
        This function is same as sendKeys, but types characters one by one with a
        delay
        """
        delay = kwargs["delay"] if "delay" in kwargs else self.typeDelay

        def sendKey(byteseq):
            with open("/dev/hidg0", "wb+") as f:
                f.write(byteseq.ljust(8, b"\x00"))
                f.write(b"\x00" * 8)

        for arg in args:
            with open("/dev/hidg0", "wb+") as f:
                if isinstance(arg, str):
                    for c in arg:
                        code, shifted = self.convert(c)
                        byteseq = bytes([2 if shifted else 0, 0, code])
                        sendKey(byteseq)
                        sleep(delay)
                elif isinstance(arg, int):
                    byteseq = bytes([0, 0, arg])
                    sendKey(byteseq)
                    sleep(delay)
        sleep(self.execDelay)

    def sendCombo(self, *args, **kwargs):
        mod = 0
        if "mod" in kwargs and kwargs["mod"]:
            if isinstance(kwargs["mod"], list):
                for modkey in kwargs["mod"]:
                    mod |= modkey
            else:
                mod = kwargs["mod"]

        keys = []
        for arg in args:
            keys += [arg] if isinstance(arg, int) else [self.convert(c)[0] for c in arg]

        byteseq = bytes([mod, 0] + keys[:6]).ljust(8, b"\x00")
        with open("/dev/hidg0", "wb+") as f:
            f.write(byteseq)
            f.write(b"\x00" * 8)

        sleep(self.execDelay)
