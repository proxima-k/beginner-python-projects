import datetime
import time

dict_month = {"Jan"     : 1,
              "Feb"     : 2,
              "March"   : 3,
              "Apr"     : 4,
              "May"     : 5,
              "June"    : 6,
              "July"    : 7,
              "Aug"     : 8,
              "Sept"    : 9,
              "Oct"     : 10,
              "Nov"     : 11,
              "Dec"     : 12}

list_month = ["Jan",
              "Feb",
              "March",
              "Apr",
              "May",
              "June",
              "July",
              "Aug",
              "Sept",
              "Oct",
              "Nov",
              "Dec"]

def time_change():
    if interval_.lower() == "h":
        time_chn = time_int * 3600
    elif interval_.lower() == "m":
        time_chn = time_int * 60
    else:
        time_chn = time_int
    return time_chn

def tdelta():
    dt_future = datetime.datetime(year_f, month_f, day_f, hour_f, minute_f, second_f, 0)
    dt_now = datetime.datetime.now()
    time_delta = dt_future - dt_now
    return time_delta


input("Welcome to the Countdown Clock! Type anything to continue.")
interval_ = input("What unit do you want to be notified about the time left?\nHours(h), Minutes(m),Seconds(s)\n")
time_int = float(input("At what intervals should I print out the time left?\n"))
time_int = time_change()

print("Now, what's your desired time?")


year_f = int(input("The year?\n"))                      #todo: fix error, maybe while loops?
month_f = input("The month?(You can type in the form of Jan, Feb, etc. or 1, 2, etc.)\n")
day_f = int(input("The date?\n"))
hour_f = int(input("The hour?\n"))      #absolute hour
minute_f = int(input("The minute?\n"))
second_f = int(input("The second?\n"))
# us_f = int(input("The microsecond?\n"))


if month_f.capitalize() in list_month:
    month_f = dict_month[month_f.capitalize()]
elif int(month_f) in range(1, 13):
    month_f =  int(month_f)
else:
    print("Error, input not found.")


if tdelta().total_seconds() > 0:            #todo: if intererval = 5, time left 4. What to do?       ##done

    dt_delta = tdelta()

    while dt_delta.total_seconds() > 0:
        dt_delta = tdelta()
        print(dt_delta)


        if dt_delta.total_seconds() > time_int:
            time.sleep(time_int)
            dt_delta = tdelta()
        else:
            time.sleep(dt_delta.total_seconds())
            dt_delta = tdelta()
    print("Time's Up!!")

elif tdelta().total_seconds() < 0:
    print("The time you inserted has passed.Please start again :)")

else:
    print("Error, please start over.")

input("Type anything to exit.\n")