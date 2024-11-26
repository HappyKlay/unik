from abc import ABC, abstractmethod

class Image(ABC):
    @abstractmethod
    def display(self):
        pass
class RealImage(Image):
    def __init__(self, filename: str):
        self.filename = filename
        self.load_image()

    def load_image(self):
        print(f"Loading image: {self.filename}")

    def display(self):
        print(f"Displaying image: {self.filename}")
class ImageProxy(Image):
    def __init__(self, filename: str):
        self.filename = filename
        self.real_image = None

    def display(self):
        if self.real_image is None:
            self.real_image = RealImage(self.filename)
        self.real_image.display()
# Створюємо проксі
image1 = ImageProxy("image1.jpg")
image2 = ImageProxy("image2.jpg")

# Перший доступ до зображення (реальне зображення завантажується і відображається)
image1.display()

# Другий доступ до того ж зображення (реальне зображення не завантажується знову)
image1.display()

# Перший доступ до іншого зображення (нове завантаження)
image2.display()
