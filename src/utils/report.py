import time

TARGET_ESSID = None
TARGET_KEY = None
TARGET_BSSID = None
TARGET_CHANNEL = None
TARGET_PRIVACY = None

file = open("log.html", "w")
file.write('<h1> REPORTE </h1>')
file.close()

def saveLog(data):
	file = open("log.html", "a")
	file.write('<h3>' + time.strftime("%H:%M:%S") + ' [ ' + data + ' ] </h3>')
	file.close()
	


