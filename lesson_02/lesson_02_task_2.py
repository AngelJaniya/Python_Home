def is_year_leap(year):
    return year % 4 == 0


example = 2025
result = is_year_leap(example)
print('год ' + str(example) + ':', result)
