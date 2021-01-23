from hid import Keyboard
from hid.KEYS import META, ENTER, CTRL, UP, DOWN, LEFT, RIGHT, ALT, TAB, F6, SHIFT, HOME
from time import sleep

kb = Keyboard()

kb.sendCombo("r", mod=META)
kb.typeKeys("notepad", ENTER)
# kb.typeKeys("Hello World! 012345: This is a tilde (~)")
# kb.sendKeys(ENTER, "This is probably super fast")
# kb.typeKeys(ENTER, "This should technically type slowly")
# kb.typeKeys(ENTER, "Tortoise mode", delay=0.5)
kb.typeKeys("Hey there!", ENTER)
kb.sendCombo("r", mod=META)
kb.typeKeys("firefox", ENTER)
kb.sendCombo(RIGHT, mod=META)
kb.sendCombo(ENTER)
sleep(0.5)
kb.execDelay = 0.4
kb.sendCombo(TAB, mod=ALT)
kb.sendKeys("https://www.youtube.com/watch?v=_r2o3NdsfOA", ENTER)
sleep(3)
kb.sendKeys(" ")
kb.sendCombo("t", mod=CTRL)
kb.sendKeys("https://github.com/radiantly", ENTER)
kb.sendCombo(TAB, mod=ALT)
kb.sendKeys("\n" * 5)
kb.typeKeys("I'm Joshua T.\n\n", delay=0.2)
kb.sendCombo(TAB, mod=ALT)
kb.sendCombo(F6)
kb.sendKeys("https://radiantly.github.io", ENTER)
kb.sendCombo(TAB, mod=ALT)
kb.typeKeys("I'm an avid NodeJS and Python programmer, tech enthusiast and CTF player.")

kb.sendCombo(TAB, mod=ALT)
kb.sendCombo("t", mod=CTRL)
kb.sendKeys("https://github.com/Jason13201", ENTER)
kb.sendCombo(TAB, mod=ALT)
kb.sendKeys("\n" * 5)
kb.typeKeys("And I'm Jason H!\n\n", delay=0.2)

# Feel free to change
kb.typeKeys(
    "I'm a pro hacker, you'll probably find me hanging around in MLH hackathons and CTFs too!"
)

kb.sendCombo("a", mod=CTRL)

kb.sendKeys("\n" * 6)
kb.typeKeys("Together, we've worked on a lot of projects")
kb.sendCombo(TAB, mod=ALT)
kb.sendCombo(F6)
kb.sendKeys("https://devpost.com/software/hackerdash", ENTER)
kb.sendCombo(TAB, mod=ALT)
kb.typeKeys("\n\n<-- HackerDash!")
kb.sendKeys(
    "\n(A dashboard for hackers that keeps them informed of the latest news and hackathons)"
)

kb.sendCombo(TAB, mod=ALT)
kb.sendCombo(F6)
kb.sendKeys("https://the-redirector.senorita.workers.dev", ENTER)

kb.sendCombo(TAB, mod=ALT)
kb.sendCombo(HOME, mod=SHIFT)
for i in range(3):
    kb.sendCombo(UP, mod=SHIFT)

kb.typeKeys("\n<-- The Redirector")
kb.sendKeys("\n(A custom metadata link shortener built on CloudFlare Workers)")

kb.sendCombo(TAB, mod=ALT)
kb.sendCombo(F6)
kb.sendKeys("https://devpost.com/software/hackshare-tn675b", ENTER)

kb.sendCombo(TAB, mod=ALT)
kb.sendCombo(HOME, mod=SHIFT)
for i in range(3):
    kb.sendCombo(UP, mod=SHIFT)

kb.typeKeys("\n<-- Hack it, share it!")
kb.sendKeys(
    "\n(A cross-platform flutter app that helps you share tips and tricks with the world)"
)
