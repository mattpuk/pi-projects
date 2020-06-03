# pi-projects
## Various Hobby projects for the Pi


First project file is a Python script [dfrobot-weatherstation-rpi.py](../master/dfrobot-weatherstation-rpi.py)
that does Serial comms between a RaspberryPi 3 and the DFRobot Anenometer/WeatherStation SKU:SEN0186 Does some transformation of the data as it comes in to make it human readable instead of the:

 ``c000s000g000t086r000p000h53b10020`` - that is output when comms are established
 
 ``It outputs 37 bytes per second, including the end CR/LF. Data Parser:
 c000s000g000t086r000p000h53b10020
c000
s000
g000
t086
r000
p000
h53
b10020 atmosphere,0.1 hpa``
 
 I copied the mathematic forumlas from the [DFRobot Arduino Sketch](https://www.dfrobot.com/wiki/index.php/Weather_Station_with_Anemometer/Wind_vane/Rain_bucket_SKU:SEN0186) To help me figure out wind speed,etc and broke them up for Python on the Pi. 
 
 Its not very elegant and needs improvement but it does work!
 
 
 


