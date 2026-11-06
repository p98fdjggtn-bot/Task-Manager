class Device:
    def __init__(self, name):
        self.name = name

    def turn_on(self):
        print(f"{self.name} is turned on")

    def turn_off(self):
        print(f"{self.name} is turned off")


class Phone(Device):
    def __init__(self, name, brand):
        Device.__init__(self, name)
        self.brand = brand

    def call(self):
        print(f"{self.brand} phone is calling")


class Laptop(Device):
    def __init__(self, name, processor):
        Device.__init__(self, name)
        self.processor = processor

    def work(self):
        print(f"{self.name} with {self.processor} is working")


phone = Phone("Phone", "Apple")
laptop = Laptop("Laptop", "Intel")

phone.turn_on()
phone.call()
phone.turn_off()

laptop.turn_on()
laptop.work()
laptop.turn_off()
