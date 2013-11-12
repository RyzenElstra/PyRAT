import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
from re import split
import urllib2

class Ui_GeoIPLocator(QWidget):

	def __init__(self):
		QWidget.__init__(self)
		self.ip_dns = ""
		self.url = "http://www.iplocationfinder.com/"

		self.initUi()

	def initUi(self):
		
		self.setWindowTitle("GeoIP Locator")
		self.resize(515, 370)
		self.setMinimumSize(QSize(515, 370))
		self.setMaximumSize(QSize(515, 370))

		self.mapa = QWebView(self)
		self.mapa.load(QUrl("bg.htm"))

		etiquetaIP = QLabel(self)
		etiquetaIP.setText("IP/DNS:")
		etiquetaIP.setGeometry(QRect(10, 335, 66, 31))

		self.entradaIP = QLineEdit(self)
		self.entradaIP.setGeometry(QRect(80, 340, 213, 21))

		self.botonBuscar = QPushButton(self)
		self.botonBuscar.setText("Search")
		self.botonBuscar.setGeometry(QRect(325, 315, 181, 51))
		self.botonBuscar.setFocusPolicy(Qt.NoFocus)

		self.connect(self.botonBuscar, SIGNAL("clicked()"), self.buscaGeoIP)

	def buscaGeoIP(self):
		self.info = []

		self.ip_dns = str(self.entradaIP.text())

		if len(self.ip_dns) == 0:
			pass
		else:

			try:
				self.ip_dns = split("http://", self.ip_dns)[1]
			except:
				pass

			url = self.url + self.ip_dns
			print "\n-------------------------------------------------------"
			print url
			print "-------------------------------------------------------\n"

			f = urllib2.urlopen(url)
			self.data = f.read()
			f.close()

			try:
				self.identificaDatos()
				self.creaMapa()
				self.mapa.load(QUrl("map.htm"))
			except Exception as e:
				print e

	def obtieneSectorInfo(self):
		sector = ["""<table class="ipinfo" border="0" cellpadding="0" cellspacing="0">""",
					"</table>"]

		sectorSplitted = split(sector[0], self.data)[1]
		sectorFinal = split(sector[1], sectorSplitted)[0]

		return sectorFinal

	def identificaDatos(self):

		info = self.obtieneSectorInfo()

		isp = ["<tr><th>ISP:</th><td>", "</td></tr>", "ISP"]
		city = ["<tr><th>City:</th><td>", "</td></tr>", "City"]
		region = ["<tr><th>Region:</th><td>", "</td></tr>", "Region"]
		country = ["<tr><th>Country:</th><td><img src=", "</td></tr>", "Country"]
		timezone = ["<tr><th>Timezone:</th><td>", "</td></tr>", "Timezone"]
		longitude = ["<tr><th>Longitude:</th><td>", "</td></tr>", "Longitude"]
		altitude = ["<tr><th>Latitude:</th><td>", "</td></tr>", "Altitude"]

		patrones = [isp, city, region, country, timezone, longitude, altitude]

		for patron in patrones:

			if patron[2] == "Country":
				dataSplitted = split(patron[0], self.data)[1]
				dataFinal = split(patron[1], dataSplitted)[0]
				countryPatrones = ["alt.+title="," style.+> "]
				
				flag = split(countryPatrones[0], dataFinal)[0]
				self.flag = self.url + flag[2:-2]
				self.cambiaIcono()

				countrySplitted = split(countryPatrones[0], dataFinal)[1]
				country = split(countryPatrones[1], countrySplitted)[1]

				self.info.append("Flag: " + self.flag)
				self.info.append("Country: " + country)			

			else:
				dataSplitted = split(patron[0], self.data)[1]
				dataFinal = split(patron[1], dataSplitted)[0]
				self.info.append(patron[2] + ": " + dataFinal)

				if patron[2] == 'Altitude':
					self.altitude = dataFinal

				if patron[2] == 'Longitude':
					self.longitude = dataFinal

		for e in self.info:
			print e

	def cambiaIcono(self):
		f = urllib2.urlopen(self.flag)
		gif = open('flag.gif', 'wb')
		gif.write(f.read())
		f.close()
		gif.close()
		self.setWindowIcon(QIcon('flag.gif')) 

	def creaMapa(self):

		map = """<!DOCTYPE html "-//W3C//DTD XHTML 1.0 Strict//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8"/>
    <title>Google Maps JavaScript API Example</title>
    <script src="http://maps.google.com/maps?file=api&amp;v=2&amp;key=ABQIAAAAQQRAsOk3uqvy3Hwwo4CclBTrVPfEE8Ms0qPwyRfPn-DOTlpaLBTvTHRCdf2V6KbzW7PZFYLT8wFD0A&sensor=false"
            type="text/javascript"></script>
    <script type="text/javascript">

    function initialize() {
      if (GBrowserIsCompatible()) {
        var map = new GMap2(document.getElementById("map_canvas"));
        map.setCenter(new GLatLng( %s, %s), 13);
        map.setUIToDefault();
      }
    }

    </script>
  </head>
  <body onload="initialize()" onunload="GUnload()">
    <div id="map_canvas" style="width: 500px; height: 300px"></div>
  </body>
</html>
""" % (self.altitude, self.longitude)

		f = open("map.htm", "w")
		f.write(map)
		f.close()

	def keyPressEvent(self, e):
		if e.key() == 16777220: # Return Key
			self.buscaGeoIP()

def main():
	bg = """<html>
	<body style="margin: 0px;">
		<img style="-webkit-user-select: none; cursor: -webkit-zoom-in;" src="http://i39.tinypic.com/2luhrp.png" width="520" height="370">
	</body>
</html>
	"""

	f = open("bg.htm", "w")
	f.write(bg)
	f.close()

	app = QApplication(sys.argv)
	gil = Ui_GeoIPLocator()
	gil.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()
