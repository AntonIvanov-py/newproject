action = input("Введите операцию: ")
amount = int(input("Сколько операндов? "))
while action != "X" and action != "*" and action != "/" and action != "+" and action != "-":
    action = input("Ошибка! Введите операцию: ")
    amount = int(input("Сколько операндов? "))

symbol = ""
str_summ = ""
summ = 0
for order in range(1, amount + 1):
    if action == "+":
        str_summ += symbol
        text = "Введите операнд " + str(order) + ": "
        number = int(input(text))
        summ += number
        str_number = str(number)
        str_summ += str_number
        symbol = " + "
    elif action == "x" or action == "*":
        summ = 1
        str_summ += symbol
        text = "Введите операнд " + str(order) + ": "
        number = int(input(text))
        summ *= number
        str_number = str(number)
        str_summ += str_number
        symbol = " * "
    elif action == "/":
        str_summ += symbol
        text = "Введите операнд " + str(order) + ": "
        number = int(input(text))
        summ = number
        summ /= number
        str_number = str(number)
        str_summ += str_number
        symbol = " / "
    elif action == "-":
        str_summ += symbol
        text = "Введите операнд " + str(order) + ": "
        number = int(input(text))
        summ = number
        summ -= number
        str_number = str(number)
        str_summ += str_number
        symbol = " - "
        
result = str_summ + " = " + str(summ)
print(result)