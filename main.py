# Любые данные, переданные из консоли, воспринимаются программой как строка.
# Поэтому прежде, чем работать со значением года, надо преобразовать его в целое число.




months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь',
             'Декабрь']

# можно добавить ещё один список месяцев, но на английском: months_eng = ['january', 'february', 'march', 'april',
# 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']


# Функция, вычисляющая, високосный ли год.
def is_leap_year(year):
    if year % 4 != 0:
        is_leap = False
    else:
        is_leap = True

    if year % 100 == 0:
        is_leap = False
    if year % 400 == 0:
        is_leap = True
    return is_leap


# Функция, вычисляющая количество дней в месяце.
def get_duration(year_value, month_index):
    if month_index in [3, 5, 8, 10]:
        duration = 30
    elif month_index == 1:
        duration = 29 if is_leap_year(year_value) else 28
    else:
        duration = 31

    return duration


# Функция, печатающая даты месяца.
def print_days(days_in_month, start_day):
    print('   ' * start_day, end='')
    for day in range(1, days_in_month + 1):
        if day < 10:
            print(day, end='  ')
        else:
            print(day, end=' ')
        if (day + start_day) % 7 == 0:
            print()
    if (days_in_month + start_day) % 7 != 0:
        print()


# Функция, печатающая шапку месяца.
def print_header(year_value, month_index):
    print(months[month_index], year_value)
    print('Пн Вт Ср Чт Пт Сб Вс')


# Функция, вычисляющая день недели, который приходится на 1 января:
def get_starting_day(year):
    d = 1
    m = 13
    y = year - 1
    h = (d + (13 * (m + 1)) // 5 + y + (y // 4) - (y // 100) + (y // 400)) % 7
    return (h + 5) % 7


# Функция, вычисляющая день недели,
# на который выпадет первое число следующего месяца:
def adjust_start_day(start_day, days_in_month):
    result = (start_day + days_in_month) % 7
    return result


# Запуск программы.
def print_calendar(year):
    # Вычисляем день недели, на который приходится 1 января года year:
    start_day = get_starting_day(year)

    # В цикле вызываем необходимые функции:
    for month_number in range(12):
        print_header(year, month_number)
        duration = get_duration(year, month_number)
        print_days(duration, start_day)

        start_day = adjust_start_day(start_day, duration)
        print()

def print_month(year, month):
    # Вычисляем день недели, на который приходится 1 января года year:
    start_day = get_starting_day(year)
    number = months.index(month)
    print_header(year, number)
    # В цикле вызываем необходимые функции:
    for month_number in range(number + 1):
        duration = get_duration(year, month_number)
        previous_start_day = start_day
        start_day = adjust_start_day(start_day, duration)

    print_days(duration, previous_start_day)

if __name__ == '__main__':
  question = input('Что хотите получить, календарь на год или на один месяц: ')
  if 'год' in question.lower():
      year = int(input('Укажите год, на который надо составить календарь: '))
      print_calendar(year)
  elif 'мес' in question.lower():
      year = int(input('Укажите год, на который надо составить календарь на месяц: '))
      question_2 = input('Напишите какой месяц: ')
      print()
      print_month(year, question_2[:1].upper() + question_2[1:])
