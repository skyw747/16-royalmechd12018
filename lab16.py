import speech_recognition as sr

r=sr.Recognizer()
with sr.Microphone() as mc:
	r.adjust_for_ambient_noise(mc,duration=5)
	r.dynamic_energy_thershold = True
	print('say!!!')
	audio = r.listen(mc)

try:
	print("you said:" + r.recognize_google(audio))
except sr.UnknownValueError:
	print("I didn't get that!")
except sr. RequestError as e:
	print('could connect to google: {0}'.format(e))	