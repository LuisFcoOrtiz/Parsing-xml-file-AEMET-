#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ParseXml.py
#  
#  Copyright 2016 manrique <https:/github.com/luisFcoOrtiz>
#  
#  python class to read AEMET XML file
# 
from xml.dom import minidom
import urllib

class ParseXml():
			
	def openUrl(self):
		#open url with xml file
		url = urllib.urlopen('http://www.aemet.es/xml/municipios/localidad_18127.xml') 
		global doc
		doc = minidom.parse(url)
		#get data in variables
		global name
		name = doc.getElementsByTagName("nombre")[0]
		global enlace
		enlace = doc.getElementsByTagName("enlace")[0]
		global etiquetaDia
		etiquetaDia = doc.getElementsByTagName("dia")
	def getName(self):
		return name.firstChild.data
	def getUrl(self):
		return enlace.firstChild.data
	#get all attributes from each day tag in XML file
	def printAttributes(self):
		for dia in etiquetaDia:
			#get attributes from each day tag (fecha,probabilidad prec, temp max, temp min)
			date = dia.getAttribute("fecha")	
			probPrecip = dia.getElementsByTagName("prob_precipitacion")[0]
			tempMax = dia.getElementsByTagName("maxima")[0]
			tempMin = dia.getElementsByTagName("minima")[0]
			try:
				print("\nfecha: %s | prob general lluvia: %s | temp Max:%s | temp Min:%s" % (date, probPrecip.firstChild.data, tempMax.firstChild.data, tempMin.firstChild.data))				
			except:
				pass
#End class	
			
