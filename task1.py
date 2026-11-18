from datetime import datetime


def get_days_from_today(date):   
    input_date = datetime.strptime(date, "%Y-%m-%d")
    today = datetime.now()
    delta = today - input_date

    return delta.days

#Test
print(get_days_from_today("2026-10-09"))
print(get_days_from_today("2026-12-09"))