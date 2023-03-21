import ShantingYard

def getK() -> int:
    while True:
        k = input("Введите k: ")
        if k.isdigit() and int(k) >= 3:
            return int(k)
        else:
            print("Неверное значение!!!")

def getN() -> int:
    while True:
        n = input("Введите n: ")
        if n.isdigit() and (int(n) == 1 or int(n) == 2):
            return int(n)
        else:
            print("Неверное значение!!!")

def getInt() -> int:
    while True:
        try:
            number = int(input())
            return number
        except ValueError:
            print("Неверное значение")

def getFunc() -> list:
    while True:
        func_str = input("Введите функцию: ")
        func_postfix = ShantingYard.getPostfixNotation(func_str)

        return func_postfix