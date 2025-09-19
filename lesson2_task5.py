def month_to_season(month):
    if month <3 or month == 12:
        print("Зима")
    elif month > 2 and month < 7:
        print("Весна")
    elif month > 6 and month < 9:
        print(" Лето")
    elif month > 8 and month < 12:
        print("Осень")
    else:
        print("Не больше 12 месяцев")


month_to_season(5)