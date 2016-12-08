import IOT
IOT.init()

def toggle():
  light = IOT.selectNearest("light")
  light.setLight(!light.getLight())