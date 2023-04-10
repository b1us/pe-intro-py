# Properties

# Properties are a way to make attributes read-only or write-only.
# We can do this by using the @property decorator
# We can also use the @property decorator to make attributes read-only or write-only

class Person: # most of the time the naming is singular
    def __init__(self, name):
        self.name = name
        self._salary = 0

    def set_salary(self, salary):
        if salary < 0:
            raise ValueError("The salary can not be negative")
        self._salary = salary

    def get_salary(self):
        return round(self._salary)

p = Person("John")
# p._salary = -100
# print(p._salary) # -100 # can not be enforced to not change it
# p.set_salary(-100)
# print(p._salary) # 0
# p.set_salary(-100)
# print(p._salary) # ValueError: The salary can not be negative
p.set_salary(100)
print(p._salary) # 100
