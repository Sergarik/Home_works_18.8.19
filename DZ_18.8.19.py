tickets = int(input("Введите количество билетов: "))
total_cost = 0
for i in range(tickets):
    age = int(input("Введите возраст посетителя: "))
    if age < 18:
        price = 0
    elif 18 <= age < 25:
        price = 990
    else:
        price = 1390
    total_cost += price

if tickets > 3:
    total_cost *= 0.9
print("Сумма к оплате: ", total_cost)

