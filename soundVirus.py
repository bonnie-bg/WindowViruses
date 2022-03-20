# usr/bin/python3
from gtts import gTTS
from playsound import playsound
import os

# msg = "You have been Hacked"
# language = "en"
# obj = gTTS(text=msg, lang=language, slow=False)
# obj.save("Virus.mp3")

# for i in range(5):
#     os.system("mpg321 Virus.mp3")
#     playsound("Virus.mp3")


tts = gTTS("hello")
tts.save("hello.mp3")
