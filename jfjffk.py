import math

class Shape:
    def area(self):
        raise NotImplementedError("Должен быть реализован в подклассах")


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def __str__(self):
        return f"Прямоугольник: длина={self.length}, ширина={self.width}"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Круг: радиус={self.radius}"


def compute_area(shape):
    return shape.area()


def shaded_area(rectangle, circle):
    if circle.radius * 2 > min(rectangle.length, rectangle.width):
        print("Предупреждение: круг не помещается внутри прямоугольника по размеру!")
    return compute_area(rectangle) - compute_area(circle)



if __name__ == "__main__":
    print("Введите параметры прямоугольника:")
    length = float(input("Длина: "))
    width = float(input("Ширина: "))

    print("\nВведите параметры круга:")
    radius = float(input("Радиус: "))

    rect = Rectangle(length, width)
    circ = Circle(radius)

    print("\n" + "="*50)
    print(f"{rect}")
    print(f"Площадь прямоугольника: {compute_area(rect):.2f}")
    print()
    print(f"{circ}")
    print(f"Площадь круга: {compute_area(circ):.2f}")
    print()

    shaded = shaded_area(rect, circ)
    print(f"Площадь закрашенной области (прямоугольник - круг): {shaded:.2f}")
    print("="*50)