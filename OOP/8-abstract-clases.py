# Abstract Class
# A class that never has any instances. 
# It should not be instantiated. 
# It's meant to be a parent class, superclass, or base class for other classes.
# It's objective is solely to increase the abstraction of the code.
# To contain the common implementation detalis (attributes and methods) of the classes that inherit from it.
# Methods: other than static, instance, and class methods, abstract class can have `abstract methods.

# Abstract Method
# An abstract method is a method that is declared in an abstract class but contains no implementation yet, but it is required to be implemented in the derived classes.

# Notes:
# Theoretically, Python does not have a keyword/notion to declare an abstract class.
# We can't actualy make something abstract. We can't force it to never be able to be instantiated.

# Abstract Class Example

import random

class AbstractGame: # do not have to be named AbstractSomething, just for education purposes only.
    # Abstract method, as general as possible
    def start(self):
        while True:
            start = input("Would you like to start the game? (y/n)")
            if start.lower() == "y":
                break        
        self.play()

    def end(self):
        print("Thank you for playing!")
        self.reset()

    # Abstract method, subclasses must implement this 
    # This abstract method is not implemented here, but it only works if the subclasses implement it
    def play(self):
        raise NotImplementedError("You must provide an implementation for play() mehtod in child classes")
    
    def reset(self):
        raise NotImplementedError("You must provide an implementation for reset() mehtod in child classes")

# Concrete Subclass
class RandumGuesser(AbstractGame):
    def __init__(self, rounds):
        self.rounds = rounds
        self.round = 0

    def reset(self):
        self.round = 0

    def play(self):
        while self.round < self.rounds:
            self.round += 1

            print(f"Welcome to round {self.round}. I'm thinking of a random number between 1-10. Guess what it is:")

            random_num = random.randint(1, 10)

            while True:
                guess = int(input("Your guess: "))
                if guess == random_num:
                    print("You guessed correctly!")
                    break
                else:
                    print("Sorry, that was not correct. Try again!")

        self.end()

game = RandumGuesser(3)
game.play()