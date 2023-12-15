from datetime import datetime, timedelta

today = datetime.now()
christmas = datetime(today.year, 12, 25)

days_until_christmas = (christmas - today).days
print("There are",days_until_christmas,"days until Christmas!")