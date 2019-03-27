#!/usr/bin/python

from __future__ import print_function
from datetime import date
from datetime import datetime
from papirus import PapirusTextPos
import calendar
import urllib, json

text = PapirusTextPos(False)
fontsize = 15

#info for AIRNow
AIRNOWAPIKEY =""
LAT = "37.7749"
LONG = "-122.4194"

#set starting text position
YPOS = 0
XPOS = 0
#get the current AQI data
aqiurl ="http://www.airnowapi.org/aq/observation/latLong/current/?format=application/json&latitude="+LAT+"&longitude="+LONG+"&distance=25&API_KEY="+AIRNOWAPIKEY
#uncomment to print URL to stdout (troubleshooting/debugging)
#print (aqiurl)

response = urllib.urlopen(aqiurl)
data = json.loads(response.read())

#Add text "AQI"  at top of display
#text.AddText('AQI',30,0,10,Id='title')

for item in data:
	#uncomment print to stdout
    	#print("{}:{}:{}\n".format(item['ParameterName'],item['AQI'],item['Category']['Name']))
      #send to papirus
	text.AddText((item['ParameterName'] + ' ' + str (item['AQI']) + ' ' + item['Category']['Name']),XPOS,YPOS,fontsize,Id=item['ParameterName'])
    	YPOS = YPOS + fontsize*2; 
text.WriteAll()
