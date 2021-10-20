'''Here are some examples of using important py modules'''

# import of modules
import sys
from time import asctime, localtime, gmtime, sleep, ctime, strftime, strptime, perf_counter
from datetime import date, time, datetime
from os import  getcwd, getlogin

import dateparser

script_start = perf_counter()
print(f'Now is {asctime()} according to asctime function')
sleep(1)
print('Tic-tac..')
sleep(1)
print(f'And now is {ctime()} according to ctime function')
sleep(1)
print('Tic-tac..')
sleep(2)
print(f"It's {asctime(gmtime())} in London")
sleep(1)
print(f"So, it means it's {asctime(localtime())} in Ukraine, dear {getlogin()}.")
sleep(2)
print(strftime("Realy, it's %H o'clock now"))
sleep(2)
print(f"And now you're in the {getcwd()} directory")
sleep(2)
print(f"It's time to enter the current date in format yyyy-mm-dd, {getlogin()}")
a = strptime(input(), '%Y-%m-%d')
print(f"Hmm... Can't believe this is the {a.tm_mday} day of the {a.tm_mon} of the {a.tm_year} year")
sleep(2)
print('...')
sleep(2)
print("And what is your favorite day in life: tomorrow, today or yesterday?")
usr_fav_day = dateparser.parse(input())
print(f"So, remember {usr_fav_day.strftime('%B')} {usr_fav_day.day} because it's a great day for you!")
sleep(2)
print("But as for me, I love New Year's Eve")

# calculation of the remaining time to NY
ny = datetime(year=2022, month=1, day=1, hour=0)
rmns = ny - datetime.now()
sleep(3)
print(f"And it's {rmns} away")
sleep(2)
print(f"All these calculations made with python {sys.version}")
sleep(2)
script_end = perf_counter()
total_script_time = (script_end - script_start)
print(f"BTW, we're talking for {total_script_time} sec. So it's time to say goodbye, dear {getlogin()}")
print("Good luck!")
