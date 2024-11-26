from abc import ABC, abstractmethod

# Базовий клас для компонентів файлової системи
class FileSystemComponent(ABC):
    @abstractmethod
    def show_details(self):
        pass
class File(FileSystemComponent):
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def show_details(self):
        print(f"File: {self.name}, Size: {self.size}KB")
class Directory(FileSystemComponent):
    def __init__(self, name: str):
        self.name = name
        self.children = []

    def add(self, component: FileSystemComponent):
        self.children.append(component)

    def remove(self, component: FileSystemComponent):
        self.children.remove(component)

    def show_details(self):
        print(f"Directory: {self.name}")
        for child in self.children:
            child.show_details()
# Створення файлів
file1 = File("file1.txt", 120)
file2 = File("file2.txt", 200)

# Створення директорії
dir1 = Directory("Documents")
dir1.add(file1)
dir1.add(file2)

# Створення іншої директорії та додавання файлів
file3 = File("file3.txt", 150)
file4 = File("file4.txt", 180)
dir2 = Directory("Images")
dir2.add(file3)
dir2.add(file4)

# Створення головної директорії, яка містить інші директорії
root = Directory("Root")
root.add(dir1)
root.add(dir2)

# Виведення всіх елементів
root.show_details()
