import datetime

today = datetime.date.today()
tmp = today.strftime("%B %d, %Y")
day = datetime.datetime.today().weekday()

DAYS_OF_WEEK = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def add_variable_to_context(request):
    return {
        'date': tmp,
        'day' : DAYS_OF_WEEK[day],
        'time' : datetime.datetime.now().strftime("%H:%M"),
    }