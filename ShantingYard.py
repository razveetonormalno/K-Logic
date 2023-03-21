def getPriority(sym: str) -> int:
    # return sym == ">" if 2 else sym == "-" if 1 else 0
    return 2 if sym == ">" else 1 if sym == "-" else 0

def isOneArg(sym: str) -> bool:
    return sym == "-"

def isTwoArg(sym: str) -> bool:
    return sym == ">"

def isOperator(sym: str) -> bool:
    return sym == "-" or sym == ">"

def isOperand(sym: str) -> bool:
    return sym == "x" or sym == "y"

def isLeftAssociated(sym: str) -> bool:
    return sym == ">"

def getPostfixNotation(func_str: str) -> list:
    stack = []
    result = []

    states_dict = {
        1: "one_arg_function",
        2: "two_arg_function",
        3: "one_arg_function_or_operand"
    }
    state = states_dict[3]

    for i in range(len(func_str)):
        sym = func_str[i]
        if sym != " ":
            if isOneArg(sym):
                if state != states_dict[3]:
                    print(f"Не ожидалась функция одного аргумента или операнд на позиции {i}.")
                    return []

                while stack:
                    temp = stack[-1]
                    check_1 = isLeftAssociated(sym) and (getPriority(sym) <= getPriority(stack[-1]))
                    check_2 = not isLeftAssociated(sym) and (getPriority(sym) < getPriority(stack[-1]))
                    if isOperator(sym) and (check_1 or check_2):
                        result.append(temp)
                        stack.pop()
                    else:
                        break
                stack.append(sym)
                state = states_dict[3]
            elif isTwoArg(sym):
                if state != states_dict[2]:
                    print(f"Не ожидалась функция двух аргументов на позиции {i}.")
                    return []

                while stack:
                    temp = stack[-1]
                    check_1 = isLeftAssociated(sym) and (getPriority(sym) <= getPriority(stack[-1]))
                    check_2 = not isLeftAssociated(sym) and (getPriority(sym) < getPriority(stack[-1]))
                    if isOperator(sym) and (check_1 or check_2):
                        result.append(temp)
                        stack.pop()
                    else:
                        break
                stack.append(sym)
                state = states_dict[3]
            elif sym == "(":
                if state == states_dict[2]:
                    print(f"Ожидалась функция двух аргументов на позиции {i}.")
                    return []
                stack.append(sym)
                state = states_dict[3]
            elif sym == ")":
                if state == states_dict[1]:
                    print(f"Ожидалась функция одного аргумента или операнд на позиции {i}.")
                    return []

                flag = False
                while stack:
                    temp = stack[-1]
                    if temp == "(":
                        flag = True
                        break
                    else:
                        result.append(temp)
                        stack.pop()

                if flag is False:
                    print("Несовпадение скобок!")
                    return []
                stack.pop()
                state = states_dict[2]
            elif sym.isdigit():
                if state != states_dict[3]:
                    print(f"Не ожидалась функция одного аргумента или операнд на позиции {i}.")
                    return []

                number = ""
                while i < len(func_str) and func_str[i]:
                    number += func_str[i]
                    i += 1
                i -= 1

                result.append(number)
                state = states_dict[2]
            elif isOperand(sym):
                if state != states_dict[3]:
                    print(f"Не ожидалась функция одного аргумента или операнд на позиции {i}.")
                    return []

                result.append(sym)
                state = states_dict[2]
            else:
                print(f"Неизвестный токен: {sym}.")
                return []

    while stack:
        temp = stack[-1]
        if temp == "(" or temp == ")":
            print("Несовпадение скобок")
            return []
        result.append(temp)
        stack.pop()

    return result