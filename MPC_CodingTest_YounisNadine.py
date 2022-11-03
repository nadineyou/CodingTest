class Person(object):

    def __init__(self, initial_age):
        if isinstance(initial_age, int):
            self.age = initial_age
        else:
            raise ValueError("Age must be an integer equal to or greater than 0")


    def what_am_i(self):
        age=self.age
        if age >= 0 and age < 13:
            print("You are young...")
        elif age >= 13 and age < 18:
            print("You are a teenager...")
        elif age >= 18:
            print("You are an adult...")


    def year_passes(self):
        age=self.age
        age+=1
        return age
