def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

if __name__ == "__main__":
    print("Калькулятор")
    print("Выберите операцию: сложение, вычитание, умножение, деление")

    op = input("Введите операцию: ")
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))

    if op == "add":
        print("Результат:", add(a, b))
    elif op == "subtract":
        print("Результат:", subtract(a, b))
    elif op == "multiply":
        print("Результат:", multiply(a, b))
    elif op == "divide":
        print("Результат:", divide(a, b))
    else:
        print("Неизвестная операция")