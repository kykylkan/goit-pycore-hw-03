from datetime import datetime, timedelta

# prepareing the birthdays list for next 7 days with current
def get_upcoming_birthdays(users: list) -> list:
    birthdays = []
    today_date = datetime.today().date()

    for user in users:
        # set user birthday in current year
        user_birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date().replace(year=today_date.year)

        # if birthday was, then skip it
        if(user_birthday < today_date):
            continue

        day = user_birthday.weekday()
        diff = (user_birthday - today_date).days

        # checking birthday in next 7 days with current and collecting the data
        if(diff < 7):
            # set birthday on monday, if it will be on weekday 
            user_birthday = user_birthday + timedelta(days=(7 - day)) if day in [5,6] else user_birthday
            birthdays.append({ **user, "birthday": datetime.strftime(user_birthday, "%Y.%m.%d") })

    return birthdays

# examples
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Kykylkan", "birthday": "1989.10.17"},
    {"name": "Kate", "birthday": "1995.11.20"},
    {"name": "Mr. X", "birthday": "2020.10.13"},
    {"name": "Ada", "birthday": "2021.10.14"},
    {"name": "Leon", "birthday": "2022.11.13"},
    {"name": "Aizek", "birthday": "2023.10.19"},
]

upcoming_birthdays = get_upcoming_birthdays(users)

print("This week's list of congratulations:", upcoming_birthdays)
