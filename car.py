class Car:
    def __init__(self, brand, model, speed):
        self.brand = brand
        self.model = model
        self.speed = speed

    def accelerate(self):
        self.speed += 10
        print("Speed after acceleration:", self.speed)

    def brake(self):
        self.speed -= 10
        print("Speed after braking:", self.speed)


car = Car("Toyota", "Camry", 50)

print("Brand:", car.brand)
print("Model:", car.model)
print("Speed:", car.speed)

car.accelerate()
car.brake()