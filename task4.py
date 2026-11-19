from datetime import datetime, timedelta
import calendar

def get_next_birthday(birthday_date, current_year):
    if birthday_date.month == 2 and birthday_date.day == 29 and not calendar.isleap(current_year):
        return birthday_date.replace(year=current_year, day=28)
    return birthday_date.replace(year=current_year)

def get_upcoming_birthdays(users):
    TODAY = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        BIRTHDAY_DATE = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        birthday_this_year = get_next_birthday(BIRTHDAY_DATE, TODAY.year)
        
        if birthday_this_year.weekday() >= 5:
            birthday_this_year += timedelta(days=7 - birthday_this_year.weekday())

        if birthday_this_year < TODAY:
            birthday_this_year = get_next_birthday(BIRTHDAY_DATE, TODAY.year + 1)

        days_until_birthday = (birthday_this_year - TODAY).days
        if 0 <= days_until_birthday <= 7:
            congratulation_date = birthday_this_year
            congratulation_weekday = congratulation_date.weekday()
            if congratulation_weekday >= 5:
                congratulation_date += timedelta(days= 7 - congratulation_weekday)

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
            })

    return upcoming_birthdays

#Test
users = [
    {"name": "John Doe", "birthday": "1985.11.19"},
    {"name": "Jane Smith", "birthday": "1990.11.21"},#Saturday
    {"name": "Jane Cool", "birthday": "1990.11.21"},#Sunday
    {"name": "Till Lindemann", "birthday": "1963.02.22"},
    {"name": "Tom Jenkins", "birthday": "1976.02.29"}, #Leap day
]

congratulate_date = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", congratulate_date)