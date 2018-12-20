import warnings

def fxn():
    warnings.warn("deprecated", DeprecationWarning)

with warnings.catch_warnings():
    warnings.simplefilter('default')
    
def bae():	
	from gtts import gTTS
	import os
	global a
	tts = gTTS(text=a , lang='en')
	tts.save("good.mp3")
	fxn()
	os.system("mpg321 good.mp3")
a="i love youuuu!"

bae()
	