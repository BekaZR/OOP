

class School:
    def wear_uniform(self):
        return "В школе все должны носить форму"


class University:
    def wear_uniform(self):
        return "Можно носить любую одежду, если ты студент"

school = School()
university = University()

for i in school, university:
    print(i.wear_uniform())