import datetime
import time

str1= "21/12/24"
d1 = datetime.datetime.strptime(str1, "%y/%m/%d")

while True:
      d2 = d1- datetime.datetime.now()
      print("Countdown to Xmas 2021 ", d2)
      time.sleep(5)
