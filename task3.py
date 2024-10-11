import re

# return UA phone in correct format.
# if format is uknown, phone will be removed from the list
def normalize_phone(phone_number: str) -> str:
    pref = "+"
    pattern = "\D"
    replace = ""

    # removing all except numbers
    phone_number_formated = re.sub(pattern, replace, phone_number)

    phone_length = len(phone_number_formated)

    # verify the lenght of the phone
    if phone_length < 9 or phone_length > 12:
        return ""

    #detect the phone code by phone length
    match len(phone_number_formated):
        case 9:
            pref += '380'
        case 10:
            pref += '38'
        case 11:
            pref += '3'

    return pref + phone_number_formated

#exmaples
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234566",
    "3380501234568",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "  (0) 111 22 11   "
]

# get normalized phones list without wrong numbers
sanitized_numbers = list(filter(None, [normalize_phone(num) for num in raw_numbers]))

print("Normalized phone numbers for SMS campaigns:", sanitized_numbers)