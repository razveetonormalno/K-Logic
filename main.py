import Gets

def Info():
    g, n = 4212, 19

    print(f"Пищулин Максим, группа: {g}, №{n}\n"
          f"Функция одного аргумента: {((g + n - 1) % 6 + 1)}\n"
          f"Функция двух аргументов: {((g + n - 1) % 7 + 1)}\n"
          f"Стандартная форма представления: {((g + n - 1) % 3 + 1)}\n"
          f"Унарное отрицание: -x\n"
          f"Импликация: x > y\n")

def Imp(num1: int, num2: int, k: int) -> int:
    return k-1 if num1 < num2 else k - 1 - num1 + num2

def Neg(n: int, k: int) -> int:
    return 0 if n == 0 else k - n

def matrix(func_pref: list, lines: int, n: int, k: int) -> list:
    elem = ""
    firstVar = ""
    secondVar = ""
    stack = []
    while func_pref:
        elem = func_pref[0]
        subMatrix = []
        if elem.isdigit():
            num = int(elem) % k
            for i in range(lines):
                subMatrix.append(num)
        elif elem == "x" or elem == "y":
            if firstVar == "":
                firstVar = elem
            if secondVar == "" and not (elem == firstVar):
                secondVar = elem
            if n == 1:
                for i in range(lines):
                    subMatrix.append(i % k)
            elif n == 2:
                if elem == firstVar:
                    for i in range(lines):
                        subMatrix.append(i // k)
                else:
                    for i in range(lines):
                        subMatrix.append(i % k)
        elif elem == "-":
            m1 = stack[-1]
            stack.pop()
            for i in range(lines):
                subMatrix.append(Neg(m1[i], k))
        elif elem == ">":
            m1 = stack[-1]
            stack.pop()
            m2 = stack[-1]
            stack.pop()
            for i in range(lines):
                subMatrix.append(Imp(m2[i], m1[i], k))
        stack.append(subMatrix)
        del func_pref[0]
    return stack[-1]

def first_form(stack: list, lines: int, n: int, k: int):
    print("\n1 форма:")
    form_1 = ""
    if n == 1:
        for i in range(lines):
            f = stack[i]
            if f != 0:
                if f != 1:
                    form_1 += "("
                    form_1 += str(f) + " & "

                form_1 += f"J_{str(i % k)}(x)"
                if f != 1:
                    form_1 += ")"
                form_1 += " v "
    else:
        for i in range(lines):
            f = stack[i]
            if f != 0:
                form_1 += "("
                if f != 1:
                    form_1 += str(f) + " & "
                form_1 += f"J_{str(i // k)}(x) & J_{str(i % k)}(y)"
                form_1 += ")"
                form_1 += " v "
    j = 1
    form_slice = tuple(map(lambda x: x.strip(), form_1[0:-3].split('v')))
    length = len(form_slice)
    with open("out.txt", "a") as file:
        print("\n1 форма:", file=file)
        for i in form_slice:
            if j == length:
                print(i)
                print(i, file=file)
            else:
                print(i + " v ", end="")
                print(i + " v ", end="", file=file)
            if j % 3 == 0:
                print()
                print(file=file)
            j += 1

def class_belongs(stack: list, lines: int, n: int, k: int) -> bool:
    print("\nПринадлежность классу")
    print("Введите количество элементов множества: ")
    eSize = Gets.getInt()
    E = []
    print("Введите значения: ")
    for i in range(eSize):
        temp = Gets.getInt()
        while temp in E:
            temp = Gets.getInt()
        E.append(temp)

    conts = True
    if n == 1:
        for i in range(lines):
            f = stack[i]
            var1 = i % k
            if var1 in E:
                if not (f in E):
                    conts = False
                    break
    else:
        for i in range(lines):
            f = stack[i]
            var1 = i // k
            var2 = i % k
            if var1 in E and var2 in E:
                if not (f in E):
                    conts = False
                    break

    return conts

def main():
    Info()
    k = Gets.getK()
    n = Gets.getN()
    lines = k**n

    func_pref = Gets.getFunc()
    # print(*func_pref)

    stack = matrix(func_pref, lines, n, k)
    with open("out.txt", "w"):
        pass

    print("\nPrint")
    with open("out.txt", "a") as file:
        print("Print", file=file)
        if n == 1:
            print("x f")
            print("x f", file=file)
            for i in range(lines):
                print(f"{i % k} {stack[i]}")
                print(f"{i % k} {stack[i]}", file=file)
        else:
            print("x y f")
            print("x y f", file=file)
            for i in range(lines):
                print(f"{i // k} {i % k} {stack[i]}")
                print(f"{i // k} {i % k} {stack[i]}", file=file)

    first_form(stack, lines, n, k)

    bel = class_belongs(stack, lines, n, k)
    with open("out.txt", "a") as file:
        if not bel:
            print("Функция не принадлежит классу T(E)")
            print("\nФункция не принадлежит классу T(E)", file=file)
        else:
            print("Функция принадлежит классу")
            print("\nФункция принадлежит классу", file=file)

if __name__ == '__main__':
    main()