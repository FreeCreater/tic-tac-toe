class Car:
    def __init__(self, speed, wheels):
        self.speed = speed
        self.wheels = wheels

    def info(self):
        print(self.speed, self.wheels)

class SportCar(Car):
    
    def __init__(self, speed, wheels, driver):
        super().__init__(speed, wheels)
        self.driver = driver 

    def info(self):
        print(self.driver)
        super().info()

    def speedUp(self):
        self.speed+=40

mashina = Car(100, 6)
mashina.info()
sportCar = SportCar(200, 1, "Unknowhn")
sportCar.speedUp()
sportCar.info()