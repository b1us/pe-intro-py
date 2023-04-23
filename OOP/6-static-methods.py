# Static Methods

# Static methods are methods that are bound to a class and not the object of the class (instance).
# Have no access to the class (cls) nor the instance (self)

class Student:
    grade_bump = 2.0

    def __init__(self, name, grades=[]):
        self.name = name
        self.grades = grades

    @classmethod
    def average_grades_bump(cls, grades):
        average = cls.average_grades(grades)
        return min(average + cls.grade_bump, 100)

    @staticmethod
    def average_grades(grades):
        return sum(grades) / len(grades)
    

s1 = Student('John', [90, 80, 70])
s2 = Student('Jane', [100, 90, 80])
print(s1.average_grades(s1.grades)) # 80.0
print(s2.average_grades(s2.grades)) # 90.0
print(Student.average_grades(s1.grades + s2.grades)) # 85.0

# Static Attributes

# Static attributes are attributes that are bound to a class.
# They are the same as class attributes.