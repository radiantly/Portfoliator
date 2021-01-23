from hid import Keyboard
from hid.KEYS import META, ENTER, CTRL, UP, DOWN, LEFT, RIGHT, ALT, TAB
from time import sleep

kb = Keyboard()

kb.sendCombo("r", mod=META)
kb.typeKeys("notepad", ENTER)
# kb.typeKeys("Hello World! 012345: This is a tilde (~)")
# kb.sendKeys(ENTER, "This is probably super fast")
# kb.typeKeys(ENTER, "This should technically type slowly")
# kb.typeKeys(ENTER, "Tortoise mode", delay=0.5)
kb.typeKeys("Hey there!")
kb.sendCombo("r", mod=META)
kb.typeKeys("firefox", ENTER)
kb.sendCombo(RIGHT, mod=META)
kb.sendCombo(ENTER)
kb.sendCombo(TAB, mod=ALT)
kb.sendKeys("https://www.youtube.com/watch?v=_r2o3NdsfOA", ENTER)
sleep(3)
kb.sendKeys(" ")
kb.sendCombo("t", mod=CTRL)
kb.sendKeys("https://github.com/radiantly", ENTER)
