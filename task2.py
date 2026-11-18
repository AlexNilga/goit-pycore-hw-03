import random


def get_numbers_ticket(min, max, quantity):
    if min < 1 or max >1000 or quantity > (max - min + 1):
        raise ValueError("Prameters are out of range or quantity is too large.")
    
    numbers = []
    while len(numbers) < quantity:
        number = random.randint(min, max)
        if number not in numbers:
            numbers.append(number)
    return numbers

#Test
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)