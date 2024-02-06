# Home_works_18.8.19
Python Code:

num_tickets = int(input('Введите количество билетов: '))
total_price = 0
for i in range(num_tickets):
    age = int(input(f'Введите возраст посетителя {i+1}: ' ))
    if age < 18:
        total_price += 0
    elif 18 <= age < 25:
        total_price += 990
    else:
        total_price += 1390
if num_tickets > 3:
    total_price *= 0.9
print('Сумма к оплате:', total_price, 'руб.')
