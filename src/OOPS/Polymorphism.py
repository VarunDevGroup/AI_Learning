

class Book:
    def __init__(self, title, author,price):
        self.title = title
        self.author = author
        self.price = price
        self._discount = 0.1  # Private attribute

    def GetDiscount(self):
        return self._discount  # Accessing private attribute through a public method   

    def SetDiscount(self, discount):
        self._discount = discount  # Modifying private attribute through a public method   

newBook=Book("Python Programming", "John Doe", 29.99)

print(newBook.title)  # Accessing public attribute
print(newBook.author)  # Accessing public attribute
print(newBook._discount)  # Accessing public attribute
print(newBook.GetDiscount())  # Accessing private attribute through a public method (will not raise an AttributeError)  
newBook.SetDiscount(0.2)  # Modifying private attribute through a public method
print(newBook.GetDiscount())  # Accessing modified private attribute through a public method