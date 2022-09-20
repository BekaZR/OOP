

class Employee:
    def __init__(self, name, surname, created_at, position, seniority):
        self.name = name
        self.surname = surname
        self.created_at = created_at
        self.position = position
        self.seniority = seniority

teacher = Employee('Beknazar', 'Abdyldaev', '13.03.2002', 'head of the institution', 4)
manager = Employee('Nursultan','Panpanzev', '16.06.2000', 'assistant', 2)
programmer = Employee('Lev', 'Boiko', '23.02.2005', 'Middle', '2')