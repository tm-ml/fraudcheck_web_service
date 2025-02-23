from datetime import date

def to_dict(self):
    data = {column.name: getattr(self, column.name) for column in self.__table__.columns}
    data.pop("id", None)
    return data

def date_difference(date_1: date, date_2: date) -> int:
    print(type(date_1))
    print(type(date_2))
    date_diff = abs((date_2 - date_1).days)
    return date_diff

def week_of_months(date: date) -> int:
    first_day_of_month = date.replace(day=1)
    first_day_of_month_weekday = first_day_of_month.weekday()
    number_of_week = (date.day + first_day_of_month_weekday) // 7 + 1
    return number_of_week
