from datetime import datetime, timedelta

interval = 10
today = datetime.today()
time = datetime.strptime(format(today), '%Y-%m-%d %H:%M:%S.%f')
minute = time.minute
# minute = 10


# example how its work
# suppose ur interval is 10 and minitue is 32
# and remember minitue/ interval or interval/minute modulas should alwaays 0
# 10/60 = 6
# if minute > interval
# 1 * 10 = 10
# 2 * 10 = 20
# 3 * 10 = 30
# 4 * 10 = 40 > 32 --------- so minitue file number is 40
# 5 * 10 = 50
# 6 * 10 = 60
# those are file minitue number.
# else
# one = interval - minute
# mintValue = minute + one

if minute > interval:
    a = 60 / interval
    for i in range(int(a)):
        multiplyValue = interval * (i + 1)
        print('multiplyValue', multiplyValue)
        print('minute', minute)
        if multiplyValue > minute:
            print(multiplyValue)
            deltaValue = multiplyValue - minute
            mintValue = multiplyValue
            break
        else:
            print(multiplyValue)
            mintValue = multiplyValue
            deltaValue = mintValue - minute
            continue
else:
    one = interval - minute
    deltaValue = one
    mintValue = minute + one

date = today + timedelta(minutes=deltaValue)
print(today)
print(mintValue)
print(deltaValue)

year = str(date.year)
month = str(date.month)
day = str(date.day)
hour = str(date.hour)
minuteNumber = str(date.minute)
date_time_file = "file" + "-" + year + "-" + month + "-" + day + "-" + hour + "-" + minuteNumber

print(date)
print(date_time_file)