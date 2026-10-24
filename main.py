import os
import sys
import termmagic
import playsound3, playsound3.playsound3
import time

class Interface:
    def __init__(self, min_duration):
        self.voicebank:dict[str,str] = {}
        self.min_duration = min_duration

        # load
        for file in os.listdir("vb"):
            self.voicebank[file.rsplit(".",1)[0]] = "vb/"+file

        print(self.voicebank)

    def input_mora(self):
        mora = ""

        while 1:
            char = sys.stdin.read(1)
            if char == "\x7F" or char == "\b":
                print("\b \b",flush=True,end="")
                mora = mora[:-1]
                continue
            print(char,flush=True,end="")
            mora += char

            if mora[-1] in "aeiou. ":
                break
            if len(mora) == 2:
                if mora[-1] in "mng":
                    break

        return mora

    def main(self):

        md = self.min_duration
        vb = self.voicebank

        prev_sound:playsound3.playsound3.Sound = None

        while 1:
            mora = self.input_mora()

            print(" ",flush=True,end="")

            sound = vb.get(mora)

            if prev_sound:
                prev_sound.stop()

            if sound:
                prev_sound = playsound3.playsound(sound,block=False)

            time.sleep(md)

if __name__ == "__main__":
    try:
        min_duration = min(float(sys.argv[1]),0.25)
    except IndexError:
        min_duration = 0
    except ValueError:
        min_duration = 0

    termmagic.disable_buffering()
    interface = Interface(min_duration)

    try:
        interface.main()
    except KeyboardInterrupt:
        sys.exit()
    finally:
        termmagic.reset()
