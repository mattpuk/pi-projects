#!/usr/bin/env python
from gpiozero import CPUTemperature
cpu = CPUTemperature()
import http.server
import socketserver
import datetime
import time
import os
import serial
ser = serial.Serial(
	port='/dev/ttyS0',
	baudrate = 9600,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS,
	timeout=10
)
airdirections = []
airspeed1s = []
airspeed5s = []
temperatures = []
rainfall1hs = []
rainfall24hs = []
humiditys = []
barometrics = []
done = False
while not done:
    current_char = ser.read()
    # check for equals sign
    if current_char == b'c':
        airdirection = ser.read(4)
        airdirections.append(airdirection.decode('utf-8')[0:3])
        airspeed1 = ser.read(4)
        airspeed1s.append(airspeed1.decode('utf-8')[0:3])
        airspeed5 = ser.read(4)
        airspeed5s.append(airspeed5.decode('utf-8')[0:3])
        temperature = ser.read(4)
        temperatures.append(temperature.decode('utf-8')[0:3])
        rainfall1h = ser.read(4)
        rainfall1hs.append(rainfall1h.decode('utf-8')[0:3])
        rainfall24h = ser.read(4)
        rainfall24hs.append(rainfall24h.decode('utf8')[0:3])
        humidity = ser.read(2)
        humiditys.append(humidity.decode('utf-8')[0:2])
        barometric = ser.read(6)
        barometrics.append(barometric.decode('utf-8')[1:6])
    # this part will depend on your specific needs.
    # in this example, we stop after 10 readings
    # check for stopping condition and set done = True
    if len(airdirections) >= 1:
        done = True
#
    for airdirection in range(len(airdirections)):
     airdirections[airdirection] = int(airdirections[airdirection])
my_adval = ''.join(map(str, airdirections))
#print("This is the values" + my_adval)
my_int_ad = int(my_adval)
my_ad = (my_int_ad)
print ("Wind Direction:" + '%.2d' % my_ad + " Degrees")
if my_ad  == 0:
   my_dir_ad = "North"
   print (my_dir_ad)
elif my_ad == 45:
   my_dir_ad = "North East"
   print (my_dir_ad)
elif my_ad == 90:
   my_dir_ad = "East"
   print (my_dir_ad)
elif my_ad == 135:
   my_dir_ad = "South East"
   print (my_dir_ad)
elif my_ad == 180:
   my_dir_ad = "South"
   print (my_dir_ad)
elif my_ad == 225:
   my_dir_ad = "South West"
   print (my_dir_ad)
elif my_ad == 270:
   my_dir_ad = "West"
   print (my_dir_ad)
elif my_ad == 315:
   my_dir_ad = "North West"
   print (my_dir_ad)
else:
   print ("Something else happened")

##
##AirSpeedAvg1###
for airspeed1 in range(len(airspeed1s)):
    airspeed1s[airspeed1] = int(airspeed1s[airspeed1])
my_as1val = ''.join(map(str, airspeed1s))
#print("This is the AS1 value" + my_as1val)
my_float_as1 = float(my_as1val)
my_as1_initial = (my_float_as1 * 0.44704)
print ("Average Wind Speed(1min):" + '%.2f' % my_as1_initial + "m/s")

###AirSpeedAvg2###
for airspeed5 in range(len(airspeed5s)):
    airspeed5s[airspeed5] = int(airspeed5s[airspeed5])
my_as5val = ''.join(map(str, airspeed5s))
#print("This is the AS5 value" + my_as5val)
my_float_as2 = float(my_as5val)
my_as2_initial = (my_float_as2 * 0.44704)
print ("Max Wind Speed(5min):" + '%.2f' % my_as2_initial + "m/s")

###Temperature####
for temperature in range(len(temperatures)):
    temperatures[temperature] = int(temperatures[temperature])
my_temperatureval = ''.join(map(str, temperatures))
#print("This is the Temperature value" + my_temperatureval)
my_float_temp = float(my_temperatureval)
my_temp_initial = (my_float_temp - 32.00 )
my_temp_5 = (my_temp_initial * 5.00 )
my_temp_9 = (my_temp_5 / 9.00)
print ("Temperature:" + '%.2f' % my_temp_9 + " Celcius")

###Rainfall 1H###
for rainfall1h in range(len(rainfall1hs)):
    rainfall1hs[rainfall1h] = int(rainfall1hs[rainfall1h])
my_rainfall1hval = ''.join(map(str, rainfall1hs))
#print("This is the rainfall1h value" + my_rainfall1hval)
my_float_rf1h = float(my_rainfall1hval)
my_rf1h_initial = (my_float_rf1h * 25.40)
my_rf1h_next = (my_rf1h_initial * 0.01)
print ("Rainfall(1hr):" + '%.2f' % my_rf1h_next + "mm")

###Rainfall 24H###
for rainfall24h in range(len(rainfall24hs)):
    rainfall24hs[rainfall24h] = int(rainfall24hs[rainfall24h])
my_rainfall24hval = ''.join(map(str, rainfall24hs))
#print("This is the rainfall24h value" + my_rainfall24hval)
my_float_rf24h = float(my_rainfall24hval)
my_rf24h_initial = (my_float_rf24h * 25.40)
my_rf24h_next = (my_rf24h_initial * 0.01)
print ("Rainfall(24hr):" + '%.2f' % my_rf24h_next + "mm")

###Humidity###
for humidity in range(len(humiditys)):
    humiditys[humidity] = int(humiditys[humidity])
my_humidityval = ''.join(map(str, humiditys))
my_int_humidity = int(my_humidityval)
my_humidity = (my_int_humidity)
print ("Humidity:" + '%.2d' % my_humidity + "%")

###Barometric Pressure###
for barometric in range(len(barometrics)):
    barometrics[barometric] = int(barometrics[barometric])
my_barometricval = ''.join(map(str, barometrics))
#print("value of barometer:" + my_barometricval)
my_float_barometric = float(my_barometricval)
my_barometric_total = (my_float_barometric / 10.00)
print ("Barometric Pressure:" + '%.2f' % my_barometric_total + "hPa")



####WEB PAGE CREATE - Replace with httpserver eventually###
print ("<HTML><BR><BR><CENTER><H1>Matts WeatherStation - Byte version<BODY BGCOLOR=#66ffff><TABLE BORDER=1 BGCOLOR=Blue><TH BGCOLOR=White>Wind Direction:<TD BGCOLOR=Yellow>" +  my_dir_ad + "</TD></TH><TR>", file=open('/var/www/html/index.html', 'w'))
print ("<TH BGCOLOR=White>Average Wind Speed(1min):<TD BGCOLOR=Yellow>" + '%.2f' % my_as1_initial + "m/s</TD></TH><TR>", file=open('/var/www/html/index.html', 'a'))
print ("<TH BGCOLOR=White>Max Wind Speed(5min):<TD BGCOLOR=Yellow>" + '%.2f' % my_as2_initial + "m/s</TD></TH><TR>", file=open('/var/www/html/index.html', 'a'))
print ("<TH BGCOLOR=White>Temperature:<TD BGCOLOR=Yellow>" + '%.2f' % my_temp_9 + " Celcius</TD></TH><TR>", file=open('/var/www/html/index.html', 'a'))
print ("<TH BGCOLOR=White>Rainfall(1hr):<TD BGCOLOR=Yellow>" + '%.2f' % my_rf1h_next + "mm</TD></TH><TR>", file=open('/var/www/html/index.html', 'a'))
print ("<TH BGCOLOR=White>Rainfall(24hr):<TD BGCOLOR=Yellow>" + '%.2f' % my_rf24h_next + "mm</TD></TH><TR>", file=open('/var/www/html/index.html', 'a'))
print ("<TH BGCOLOR=White>Humidity:<TD BGCOLOR=Yellow>" + '%.2d' % my_humidity + "%</TD></TH><TR>", file=open('/var/www/html/index.html', 'a'))
print ("<TH BGCOLOR=White>Barometric Pressure:<TD BGCOLOR=Yellow>" + '%.2f' % my_barometric_total + "hPa</TD></TH><TR></TABLE>",  file=open('/var/www/html/index.html', 'a'))
today = datetime.datetime.now()
print ("<H1>System Temperature:" + '%2.f' % (cpu.temperature), file=open('/var/www/html/index.html', 'a'))
print ("<H3>Last Updated:", today, file=open('/var/www/html/index.html', 'a'))
print ("</BODY></HTML>", file=open('/var/www/html/index.html', 'a'))
