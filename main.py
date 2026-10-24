import os
import sys
import termmagic
import playsound3
import time

class Interface:
    def __init__(self):
        self.voicebank:dict[str,str] = {}

        # load
        for file in os.listdir("vb"):
            self.voicebank[file.rsplit(".",1)[0]] = "vb/"+file

        print(self.voicebank)

    def input_mora(self):
        mora = ""

        while 1:
            char = sys.stdin.read(1)
            print(char,flush=True,end="")
            mora += char
            if mora[-1] in "aeiou":
                break

        return mora

    def main(self):

        vb = self.voicebank

        while 1:
            mora = self.input_mora()

            print(" ",flush=True,end="")

            sound = vb.get(mora)

            if sound:
                playsound3.playsound(sound,block=False)

if __name__ == "__main__":
    termmagic.disable_buffering()
    interface = Interface()

    try:
        interface.main()
    finally:
        termmagic.reset()
