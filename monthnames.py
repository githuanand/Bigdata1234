month_names= input("enter month names:").split(',')
short_names=[month[:3].capitalize() for month in month_names]
print("month names:",month_names)
print("short names:",short_names)
