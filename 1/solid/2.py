from abc import ABC, abstractmethod

# Базовий клас для працівників
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self, hours_worked, hourly_rate):
        pass

# Клас для штатних працівників
class FullTimeEmployee(Employee):
    def calculate_salary(self, hours_worked, hourly_rate):
        return hours_worked * hourly_rate

# Клас для фрілансерів
class Freelancer(Employee):
    def calculate_salary(self, hours_worked, hourly_rate):
        return hours_worked * hourly_rate * 0.8

# Клас для розрахунку зарплати (не змінюється при додаванні нових типів)
class SalaryCalculator:
    def calculate(self, employee, hours_worked, hourly_rate):
        return employee.calculate_salary(hours_worked, hourly_rate)
