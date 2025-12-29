# --- THE ROBOT FACTORY ---
# Understanding Classes and Object-Oriented Programming (OOP)

# 1. THE BLUEPRINT (The Class)
class Robot:
    def __init__(self, name, battery_level=100):
        self.name = name
        self.battery = battery_level

    def charge(self):
        self.battery = 100
        print(f"{self.name} is now fully charged!")

# 2. THE ACTION (Creating Objects)
bot1 = Robot("Ace", 75)
bot2 = Robot("Sparky", 30)

print(f"Robot 1: {bot1.name} (Battery: {bot1.battery}%)")
bot1.charge()

# --- THE CHALLENGE (YOU DO) ---
# 1. Add a greet() method inside the class.
# 2. Make it print the robot's name and battery status.

class Robot: # Updated version
    def __init__(self, name, battery_level=100):
        self.name = name
        self.battery = battery_level
        
    def greet(self):
        print(f"Beep Boop! I am {self.name}. Battery: {self.battery}%")

bot3 = Robot("Optimus", 99)
bot3.greet()