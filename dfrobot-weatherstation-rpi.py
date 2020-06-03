#!/usr/bin/env python
import time
import serial

ser = serial.Serial(
        port='/dev/ttyS0',
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
)



while 1:
	data=ser.readline()
	split_strings = []
	n  = 4 
	for index in range(0, len(data), n):
		split_strings.append(data[index : index + n])
	###AirDirection###
	my_ad_decode = (data.decode('utf-8')[1:-34])
	my_int_ad = int(my_ad_decode)
	my_ad = (my_int_ad)
	print ("Wind Direction:" + '%.2d' % my_ad + " Degrees")
	##AirSpeedAvg1###
	my_as1_decode = (data.decode('utf-8')[5:-30])
	my_float_as1 = float(my_as1_decode)
	my_as1_initial = (my_float_as1 * 0.44704) 
	print ("Average Wind Speed(1min):" + '%.2f' % my_as1_initial + "m/s")
	###AirSpeedAvg2###
	my_as2_decode = (data.decode('utf-8')[9:-26])
	my_float_as2 = float(my_as2_decode)
	my_as2_initial = (my_float_as2 * 0.44704)
	print ("Max Wind Speed(5min):" + '%.2f' % my_as2_initial + "m/s")
	###Temperature C###	
	my_temp_decode = (data.decode('utf-8')[13:-22])
	my_float_temp = float(my_temp_decode)	
	my_temp_initial = (my_float_temp - 32.00 )
	my_temp_5 = (my_temp_initial * 5.00 )	
	my_temp_9 = (my_temp_5 / 9.00)
	print ("Temperature:" + '%.2f' % my_temp_9 + " Celcius")
	###Rainfall 1H###
	my_rf1h_decode = (data.decode('utf-8')[17:-18])
	my_float_rf1h = float(my_rf1h_decode)
	my_rf1h_initial = (my_float_rf1h * 25.40)
	my_rf1h_next = (my_rf1h_initial * 0.01)
	print ("Rainfall(1hr):" + '%.2f' % my_rf1h_next + "mm")
	###Rainfall 24H###
	my_rf24h_decode = (data.decode('utf-8')[21:-14])
	my_float_rf24h = float(my_rf24h_decode)
	my_rf24h_initial = (my_float_rf24h * 25.40)
	my_rf24h_next = (my_rf24h_initial * 0.01)
	print ("Rainfall(24hr):" + '%.2f' % my_rf24h_next + "mm")
	###Humidity###	
	my_humidity_decode = (data.decode('utf-8')[25:-11])
	my_int_humidity = int(my_humidity_decode)
	my_humidity = (my_int_humidity)
	print ("Humidity:" + '%.2d' % my_humidity + "%")
	###Barometric Pressure###
	my_barometric_decode = (data.decode('utf-8')[28:-5])
	my_float_barometric = float(my_barometric_decode)
	my_barometric_total = (my_float_barometric / 10.00)
	print ("Barometric Pressure:" + '%.2f' % my_barometric_total + "hPa")