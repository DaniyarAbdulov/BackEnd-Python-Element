class Driver:
    def __init__(self, fullname: str, experience: int):
        self.fullname = fullname
        self.experience = experience

    def __str__(self) -> str:
        return f'{self.fullname}, {self.experience}'


class Person(Driver):
    def __init__(self, fullname: str, experience: int, age: int):
        Driver.__init__(self, fullname, experience)
        self.age = age

    def __str__(self) -> str:
        return f'fullname: {self.fullname}, driving experience: {self.experience}, age: {self.age}'


class Engine:
    def __init__(self, power: int, company: str):
        self.power = power
        self.company = company

    def __str__(self) -> str:
        return f'Power: {self.power}, Company: {self.company}'


class Car:
    def __init__(self, model: str, car_class: str, weight: int, driver: Person, engine: Engine):
        self.model = model
        self.car_class = car_class
        self.weight = weight
        self.driver = driver
        self.engine = engine

    def start (self):
        return f'Drive Forward'

    def stop (self):
        return f'Stop the Vechicle'

    def turnRight (self):
        return f'Turn Right'

    def turnLeft (self):
        return f'Turn Left'

    def toString(self):
        return f'model: {self.model}, class: {self.car_class}, weight: {self.weight}, \n{self.driver}, {self.engine}'


class Lorry(Car):
    def __init__(self, model: str, car_class: str, weight: int, driver: Person, engine: Engine, carrying: int):
        super().__init__(model, car_class, weight, driver, engine)
        self.carrying = carrying


class SportCar(Car):
    def __init__(self, model: str, car_class: str, weight: int, driver: Person, engine: Engine, speed: int):
        super().__init__(model, car_class, weight, driver, engine)
        self.speed = speed


person1 = Person('John Doe', experience=25, age=50)
lorry_engine = Engine(company='Mercedes-Benz', power=500)

lorry = Lorry(car_class='Workers', model='Mercedes Carrier', weight=2500, driver=person1, carrying=120, engine=lorry_engine)
print(lorry.toString())

print('_____________________________________')

person2 = Person('Adam White', experience=9, age=27)
sport_engie = Engine(company='Tesla', power= 1200)

sport = SportCar(car_class='Sport/Business', model='Tesla model T', weight=1800, driver=person2, speed=350, engine=sport_engie)
print(sport.toString())

print('_____________________________________')

print(SportCar.start(sport))
print(SportCar.stop(sport))
print(SportCar.turnLeft(sport))
print(SportCar.turnRight(sport))


