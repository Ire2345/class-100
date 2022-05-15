class Car():
    def __init__(self, name, model, colour):
        self.name=name
        self.model=model
        self.colour=colour

    def startCar(self):
        print("The car has been started")

    
def main():
    car1=Car("Jamie", "2021 Jeep", "white")
    print(car1.colour,car1.name,car1.model)
    car2=Car("Max", "2022 Mercedes", "blue")
    print(car2.name,car2.model,car2.colour)
    car3=Car("Jasmine", "2012 Camaro", "red")
    print(car3.name,car3.model,car3.colour)
    car4=Car("Brad", "Tesla Model X", "black")
    print(car4.name,car4.model,car4.colour)
    car5=Car("Chase", "2005 Dune Buggy", "yellow")
    print(car5.name,car5.model,car5.colour)
main()



