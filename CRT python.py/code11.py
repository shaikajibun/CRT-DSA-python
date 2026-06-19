"""Question 5: Watch Class
Using your Casio Watch example.
Attributes:
brand
current_time
battery_percentage
Methods:
show_time()
light_on()
beep()"""
from datetime import datetime
class Watch:
    def __init__(self,brand):
        self.brand=brand
    def show_time(self):
        print(datetime.now())
    def beep(self):
        print("beep! beep!")
w1=Watch("casio")
print(w1.brand)
print(w1.show_time())
w1.beep()
