
class Human:
    name = "muh"
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def hello(self):
        print(f'Hello {self.name}')

class Teacher(Human):
    def __init__(self, speciality, salary, favorite_lesson):
        self.speciality=speciality
        self.salary=salary
        self.favorite_lesson=favorite_lesson


class Student(Human):
    def __init__(self,grade,favorite_lesson):
        self.grade = grade
        self.favorite_lesson = favorite_lesson

pavel=Human('Pavel',20)

teah = Teacher('programming', '10000', 'OIVT')
student=Student([5,3,4,5],'fizkultura')

print(teah.human.name)




