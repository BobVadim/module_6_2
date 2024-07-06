
class Vehical:
    def __init__(self, owner, model, engine_power, color, COLOR_VARIANTS=['red', 'black', 'green']):
        self.owner = owner
        self.model = model
        self.engine_power = engine_power
        self.color = color
        self.COLOR_VARIANTS = ['red', 'black', 'green']
    def get_model(self):
        return print(f"Модель: {self.model}")
    def get_horsepower(self):
        return print(f'Мощность двигателя: {self.engine_power}')
    def get_color(self):
        return print(f'Цвет: {self.color}')
    def print_info(self):
        print(vehicle1.get_model(), vehicle1.get_horsepower(), vehicle1.get_color(), 'Владелец: ', vehicle1.owner)
    def set_color(self, new_color):
        self.new_color = new_color
        if self.new_color not in self.COLOR_VARIANTS:
            print(f"Нельзя сменить цвет на {self.new_color}")
        else:
            self.color = self.new_color
class Sedan(Vehical):
    PASSENGERS_LIMIT = 5
vehicle1 = Sedan('Fedos', 'Toyota Mark II',500,'blue')
# vehicle1.get_model()
# vehicle1.get_horsepower()
# vehicle1.get_color()
vehicle1.print_info()
vehicle1.set_color('green')
vehicle1.print_info()