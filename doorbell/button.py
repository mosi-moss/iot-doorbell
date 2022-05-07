import time
import grovepi
import threading
import time
import requests

class Button_LED():
    def __init__(self, pin):
        self.pin = pin
        self.active = False

    def read(self):
        grovepi.pinMode(self.pin,"INPUT")
        return grovepi.digitalRead(self.pin)

    def on(self):
        if not self.active:
            grovepi.pinMode(self.pin,"OUTPUT")
            grovepi.digitalWrite(self.pin, 1)
            self.active = True

    def off(self):
        if self.active:
            grovepi.pinMode(self.pin,"OUTPUT")
            grovepi.digitalWrite(self.pin, 0)
            self.active = False

class Ranger():
    def __init__(self, pin):
        self.pin = pin

    def read(self):
        return grovepi.ultrasonicRead(self.pin)

class Buzzer():
    def __init__(self, pin):
        self.pin = pin

    def buzz(self):
        grovepi.pinMode(self.pin,"OUTPUT")
        grovepi.digitalWrite(self.pin ,1)
        time.sleep(0.5)
        grovepi.digitalWrite(self.pin ,0)


class Doorbell():
    """
    A class to access the raspberry pi doorbell.
    """
    thread = None
    ranger_pin = 4
    button_pin = 3
    buzzer_pin = 8
    last_notification = None

    def __init__(self):
        """Start the background doorbell thread if it isn't running yet."""
        if self.thread is None:
            print("Starting doorbell thread.")
            self.last_notification = time.time()
            # start background status thread
            threading.Thread(target=self.check).start()

    def check(self):
        button = Button_LED(self.button_pin)
        ultrasonic_ranger = Ranger(self.ranger_pin)
        buzzer = Buzzer(self.buzzer_pin)
        while True:
            readRanger = ultrasonic_ranger.read()
            readButton = button.read()
            if readButton == 0:
                button.on()
                buzzer.buzz()
                print("BUTTON")
                self.notify()
            elif readRanger < 50:
                print(f"RANGER {readRanger}")
                self.notify()
            time.sleep(1)
            button.off()

    def notify(self):
        if time.time() - self.last_notification > 10:
            self.last_notification = time.time()
            try:
                req = requests.get("http://0.0.0.0:5000/api/broadcast")
                print(req.json()["body"])
            except Exception as e:
                print(e)
"""
button = 3
ultrasonic_ranger = 4
# buzzer = Buzzer(self.ranger_pin)
grovepi.pinMode(button,"OUTPUT")
while True:
    sotots = grovepi.ultrasonicRead(ultrasonic_ranger)
    #status = 1
    if sotots == 0:
        status = grovepi.digitalWrite(3, 1)
        #button.on()
        # buzzer.buzz()
        print("BUTTON")
    elif(sotots < 50):
        print(f"RANGER {sotots}")
    time.sleep(1)
    status = grovepi.digitalWrite(3, 0)
    print(f"RANGER {sotots}")
"""
