from gtts import gTTS
import os
import sys
import time
def jalan(z):
    for x in z + '\n':
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(00000.1)
os.system('clear')
os.system('git pull https://github.com/khalid-bx/voice')
os.system('clear')
print("""\033[1;35m
──────────────────
──────────────────
╔╗╔╗╔══╗╔╗╔══╗╔══╗
║╚╝║║╔╗║─╣║╔═╝║║═╣
╚╗╔╝║╚╝║║║║╚═╗║║═╣
─╚╝─╚══╝╚╝╚══╝╚══╝""")
print('')
print('[0] exit')
i=input("ENTRE TEXT : ")
if i=='0':
    os.system('exit')
x="en"
xo=gTTS(text=i,lang=x,slow=False)
xo.save("/sdcard/moro.mp3")
jalan('\033[1;33mThe text has been converted into an audio clip')
os.system('cd /sdcard ; termux-open moro.mp3')
