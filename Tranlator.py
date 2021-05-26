from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import os
import warnings
warnings.filterwarnings('ignore')
dic={"tamil":"ta","hindi":"hi","japanese":"ja","french":"fr","english":"en"}
text =input("Enter the word or sentence that has to be translated : ")
lang=input("Enter the language to which it has to be translated : ")
t=Translator(service_urls=["translate.google.com"])
translation=t.translate(text,dest=dic[lang])
text1=translation.text
speech=gTTS(text=text1,lang=dic[lang])
speech.save("translate.mp3")#the audio is saved in the location of this python file
playsound("translate.mp3")
os.remove("translate.mp3")
