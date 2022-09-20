class Car:
    def __init__(self,car_model,model,created_at,color,mileage):
        self.car_model = car_model
        self.model = model
        self.created_at = created_at
        self.color = color
        self.mileage = mileage
        
    def __str__(self):
        return f'\nМарка автомобиля: {self.car_model}\nМодель автомобиля: {self.model}\nГод выпуска: {self.created_at}\nЦвет автобиля: {self.color}\nПробег: {self.mileage}\n'
    
bmw = Car('BMW', 'M5', 2021, 'blac', '1000km')
mersedes = Car('Mersedes', 'A - Class', 2021, 'White', '1050km')
print(bmw,mersedes)
