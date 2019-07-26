from machine import Pin
import camera
camera.init()
flash_light=Pin(04,Pin.OUT)
def photo(name):
    flash_light.on()
    img=camera.capture()
    flash_light.off()
    with open(name,'w') as f:
        f.write(img)
