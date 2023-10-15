# Operator Overloading

# Operator Overloading is the ability to implement custom operation on our own classes.

# Example

class Page:
    def __init__(self, words, page_number):
        self.words = words
        self.page_number = page_number

    # Dunder or magic method
    def __add__(self, other):
        new_words = self.words + other.words
        new_page_number = max(self.page_number + other.page_number) + 1
        return Page(new_words, new_page_number)


page1 = Page("Page number 1", 1)
page2 = Page("Page number 2", 2)
page3 = page1 + page2
print(page3.words, page3.page_number)
