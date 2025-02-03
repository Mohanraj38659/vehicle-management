from car import Car
from bike import Bike

def main():
    car1 = Car("Toyota", "Corolla", 2022, 4)
    bike1 = Bike("Yamaha", "R15", 2023, "Sport")

    print(car1.display_info())
    print(bike1.display_info())

if __name__ == "__main__":
    main()
