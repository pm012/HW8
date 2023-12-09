from datetime import date, datetime


def get_birthdays_per_week(users):
    current_date = date.today()
    print(current_date)
    print(datetime.now().date())
    birthdays_dict = dict()

    if len(users) == 0:
        return birthdays_dict

    for user in users:
        user_bday = user["birthday"]
        user_bday = user_bday.replace(year=current_date.year)

        if user_bday >= current_date and (user_bday - current_date).days < 7:
            day_of_week = user_bday.strftime("%A")
            dow_num = user_bday.weekday()

            # Additional check that the weekend belongs to this week.
            if dow_num in (5, 6) and (user_bday - current_date).days < 6:
                day_of_week = "Monday"
                if day_of_week in birthdays_dict:
                    birthdays_dict[day_of_week].append(user['name'])
                else:
                    birthdays_dict[day_of_week] = [user['name']]
            else:
                if day_of_week in birthdays_dict:
                    birthdays_dict[day_of_week].append(user['name'])
                else:
                    birthdays_dict[day_of_week] = [user['name']]
        elif (user_bday - current_date).days < 0:
            user_bday = user_bday.replace(year=current_date.year + 1)
            day_of_week = user_bday.strftime("%A")
            dow_num = user_bday.weekday()

            if (user_bday - current_date).days < 7:
                if dow_num in (5, 6) and (user_bday - current_date).days < 6:
                    day_of_week = "Monday"
                    if day_of_week in birthdays_dict:
                        birthdays_dict[day_of_week].append(user['name'])
                    else:
                        birthdays_dict[day_of_week] = [user['name']]
                else:
                    if day_of_week in birthdays_dict:
                        birthdays_dict[day_of_week].append(user['name'])
                    else:
                        birthdays_dict[day_of_week] = [user['name']]

    return birthdays_dict


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 12, 16).date()},
        {"name": "Jan Clode", "birthday": datetime(1976, 12, 16).date()},
        {"name": "Van Dam", "birthday": datetime(1976, 12, 9).date()},
        {"name": "Bruce Lee", "birthday": datetime(1976, 12, 6).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)

    # Display the result
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
