# this file holds all required functions

import calendar


def provide_calendar(year: int):
    y = year
    for m in range(1, 13):
        print(calendar.month(y, m))
    return True


def provide_month(year: int, month: int):
    y = year
    m = month
    print(calendar.month(y, m))
    return True


if __name__ == '__main__':
    # provide_calendar(2024)
    provide_month(2022, 6)
