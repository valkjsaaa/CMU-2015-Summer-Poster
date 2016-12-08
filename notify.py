import IOT
IOT.init()

for light in IOT.selectAll("light"):
	def blink(): light.on(); light.off(); light.on();
	light._createMethod("notify", blink, {}, "notify the user")

for speaker in IOT.selectAll("speaker"):
	def say(): speaker.speak("You have a notification!")
	speaker._createMethod("notify", say, {}, "notify the user")

def notify():
	IOT.selectAll().notify()