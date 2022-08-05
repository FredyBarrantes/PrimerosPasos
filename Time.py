import datetime
"""from datetime import date
#(year,month,day) if is not typed any data is set 0.
fecha = datetime.date(2022,8,1)
print(fecha)"""

"""from datetime import time
#(hour,minutes,seconds,microsecond) if is not typed any data is set to 0.
hora = datetime.time(15,10,30,2200)
print(hora)"""

"""#(year,month,day,hour,minutes,seconds,microseconds)
fecha_hora = datetime.datetime(2022,8,1,15,17,45,50000)
print(fecha_hora)
cumpleanos = datetime.datetime(1987,12,15,5,18)
print(cumpleanos)
#time diference between fecha_hora and cumpleanos.
tiempo = fecha_hora - cumpleanos
print(tiempo)
#type shows that the data inside of tiempo is timedelta.
print(type(tiempo))"""

#Exercise

"""To calculate the time difference between the current date (today) and your birthday.
To do this, set today as the first timestamp, and your birthday as the second timestamp."""

#now() method that gives the current local date and time.
hoy = datetime.datetime.now()
cumple = datetime.datetime(1987,12,15,5,18)
tiem_dif = hoy - cumple
print("Your birthday is in",tiem_dif)
#take just days.
tiem_dias = tiem_dif.days
print("Your birthday is in",tiem_dias,"days.")
#take just seconds.
tiem_seg = tiem_dif.total_seconds()
print("Your birthday is",tiem_seg,"seconds away.")
#How to find time difference in minutes.
tiem_min = tiem_seg/60
print("Your birthday is",tiem_min,"minutes away.")
#How to find time difference in hours.
tiem_horas = tiem_seg/(60*60)
print("Your birthday is",tiem_horas,"hours away.")