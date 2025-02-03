from vehicle import Vehicle

class Bike(Vehicle):
    def __init__(self, make, model, year, type_of_bike):
        super().__init__(make, model, year)
        self.type_of_bike = type_of_bike

    def display_info(self):
        return f"{super().display_info()} ({self.type_of_bike})"
