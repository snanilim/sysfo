from datetime import datetime, timedelta

interval = 2
today = datetime.today()
time = datetime.strptime(format(today), '%Y-%m-%d %H:%M:%S.%f')
minute = time.minute
# minute = 10

if minute > interval:
    a = 60 / interval
    for i in range(int(a)):
        mapo = interval * (i + 1)
        print('mapo', mapo)
        print('minute', minute)
        if mapo > minute:
            print(mapo)
            mintValue = mapo
            break
        else:
            print(mapo)
            mintValue = mapo
            continue
else:
    one = interval - minute
    mintValue = interval + one

# date = today + timedelta(minutes=mintValue)
print(today)
print(mintValue)