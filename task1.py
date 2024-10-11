from datetime import datetime

# calculates the number of days between the specified date and the current date.
# date param - YYYY-MM-DD
# return - count of days or none
def get_days_from_today(date: str) -> int|None:
    date_converted = None

    try:
        date_converted = datetime.strptime(date, '%Y-%m-%d')
    except Exception:
        print("Wrong date format")
        return None
    
    return (datetime.today() - date_converted).days

#example
some_date = '2022-02-24'

result = get_days_from_today(some_date)

print(f"Count of days: {result}")