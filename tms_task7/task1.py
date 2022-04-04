class Vehicle:
    def __init__(self, brand, model, type):
        self.brand = brand
        self.model = model
        self.type = type

    def drive(self):
        print(f'The {self.model} is now driving..')

skoda_fabia = Vehicle(
    brand = 'Skoda',
    model = 'Fabia',
    type = 'Sedan'
)

class Electric(Vehicle):
    def __init__(self, battery_capacity: float, **kwargs):
        self.battery_capacity = battery_capacity
        super().__init__(**kwargs)
    def drive(self):
        super().drive()
        print('..and driving really fast!')

tesla_x = Electric(
    brand = 'Tesla',
    model = 'Model X',
    type = 'Sedan',
    battery_capacity = 100.0
)
tesla_x.drive()