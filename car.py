from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors

    def display_info(self):
        return f"{super().display_info()} with {self.doors} doors"
