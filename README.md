# pi-projects
## Various Hobby projects for the Pi


First project file is a Python script [dfrobot-weatherstation-rpi.py](../master/dfrobot-weatherstation-rpi.py)
that does Serial comms between a RaspberryPi 3 and the DFRobot Anenometer/WeatherStation SKU:SEN0186 Does some transformation of the data as it comes in to make it human readable instead of the:

 ``c000s000g000t086r000p000h53b10020`` - that is output when comms are established
 
 I copied the mathematic forumlas from the [DFRobot Arduino Sketch](https://www.dfrobot.com/wiki/index.php/Weather_Station_with_Anemometer/Wind_vane/Rain_bucket_SKU:SEN0186)
 
 and broke them up for Python on the Pi. Its not very elegant and needs improvement but it does work!
 
 


