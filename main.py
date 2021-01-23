from hid import Keyboard
from hid.KEYS import META, ENTER

kb = Keyboard()

kb.sendCombo(META, "r")
kb.typeKeys("notepad", ENTER)
kb.typeKeys("Hello World! 012345: This is a tilde (~)")
kb.sendKeys(ENTER, "This is probably super fast")
kb.typeKeys(ENTER, "This should technically type slowly")
kb.typeKeys(ENTER, "Tortoise mode", delay=0.5)
