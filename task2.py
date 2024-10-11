import random

# return unique list of numbers or empty list
# min, max, quantinty - only numbers
def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    list = []

    # trying to cnovert params into int
    try:
        min = int(min)
        max = int(max)
        quantity = int(quantity)
    except Exception:
        return []

    # check params
    if min < 1 or max > 1000 or max - min < quantity:
        return []

    # filling the unique numbers list
    while len(list) < quantity:
        random_int = random.randint(min, max)

        if random_int not in list:
            list.append(random_int)

    return sorted(list)

lottery_numbers = get_numbers_ticket(1, 36, 6)

print(f"Your lottery numbers: {lottery_numbers}")