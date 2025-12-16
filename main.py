# 3. Shakllar ierarxiyasi

class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
# 4. Transport vositalari

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        return "Transport ishga tushdi"


class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors


class Motorcycle(Vehicle):
    def __init__(self, brand, model, has_sidecar):
        super().__init__(brand, model)
        self.has_sidecar = has_sidecar


# 5. Kitob turlari

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Ebook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size


class PrintedBook(Book):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.pages = pages


class AudioBook(Book):
    def __init__(self, title, author, duration):
        super().__init__(title, author)
        self.duration = duration
