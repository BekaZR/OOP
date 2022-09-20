

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_my_name(self):
        print(f'Здравствуйте, меня зовут {self.name}')


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    @classmethod
    def grades(cls):
        print('5, 4, 5, 3, 4')
    
    def show_grade(self):
        Student.grades()


class Theacher(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        
    def say_my_name(self):
        print('Профессор')
        super().say_my_name()


beka = Person('Beka', 20)
student = Student('Lev',17)
theacher = Theacher('Nurs',20)

beka.say_my_name()
student.show_grade()
theacher.say_my_name()
