import pyttsx3

engine = pyttsx3.init()


rate = engine.getProperty('rate')
volume = engine.getProperty('volume')

engine.setProperty('rate', rate-15)
engine.setProperty('volume', volume-0.25)


y =1

while y > 0:
	intxt = input()
	x = intxt.lower()
	if x == ("exit"):
		break
	
	engine.say(x)
	engine.runAndWait()
	

