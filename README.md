# pi-projects
## Various Hobby projects for the Pi


First project file is a Python script [dfrobot-weatherstation-rpi.py](../master/dfrobot-weatherstation-rpi.py)
that does Serial comms between a RaspberryPi 3 and the DFRobot Anenometer/WeatherStation SKU:SEN0186 Does some transformation of the data as it comes in to make it human readable instead of the:

 ``c000s000g000t086r000p000h53b10020`` - that is output when comms are established
 
Taken from the DFRobot Arduino how-to:

#### It outputs 37 bytes per second, including the end CR/LF. Data Parser:
 
```c000s000g000t086r000p000h53b10020
c000 - air direction, degree
s000 - air speed(1 minute), 0.1 miles per hour
g000 - air speed(5 minutes), 0.1 miles per hour
t086 - temperature, Fahrenheit
r000 - rainfall(1 hour), 0.01 inches
p000 - rainfall(24 hours), 0.01 inches
h53 -  humidity as percentage
b10020 - atmosphere,0.1 hpa
```
  
  
 
 I copied the mathematic forumlas from the [DFRobot Arduino Sketch](https://www.dfrobot.com/wiki/index.php/Weather_Station_with_Anemometer/Wind_vane/Rain_bucket_SKU:SEN0186) To help me figure out wind speed,etc and broke them up for Python on the Pi. 
 
 Its not very elegant and needs improvement but it does work!
 
 
 


