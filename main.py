from datetime import date, datetime


def get_birthdays_per_week(users):
    current_date = datetime.now()
    next_week_interval = datetime.timedelta(weeks=1)
    for user in users.iter():
        user_bday = user["birthday"]

        if user["birthday"] in next_week_interval:
            pass


    # Реалізуйте тут домашнє завдання


    return users


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")