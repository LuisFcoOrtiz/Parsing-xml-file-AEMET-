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
import os
class ParseXml():
	
	#Check if network connection is possible
	def checkConnection(self):
		hostname = "8.8.8.8"
		response = os.system("ping -q -c 1 " + hostname + " > /dev/null")
		#and then check the response...
		if response == 0:
		  return True		#network connect is ok
		else:
		  return False		#network connect is unracheable
	
	def setUrl(self, urlEntry=''):
		global xmlFileFromUrl 
		xmlFileFromUrl = urlEntry
		
	def openUrl(self):
		#open url with xml file
		url = urllib.urlopen(xmlFileFromUrl) 
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
				fecha = date
				probabilidad = probPrecip.firstChild.data
				maxima = tempMax.firstChild.data
				minima = tempMin.firstChild.data
				print("\nfecha: %s | prob general lluvia: %s | temp Max:%s | temp Min:%s" % (date, probPrecip.firstChild.data, tempMax.firstChild.data, tempMin.firstChild.data))				
			except:
				pass									
	
	#Get all dates
	def getAllDates (self):
		print("Fechas posibles")
		for dia in etiquetaDia:					
			date = dia.getAttribute("fecha")			
			print("| %s |" % (date))
			
			
	def LookForADay (self, day=''):		
		for dia in etiquetaDia:					
			#get one day in especific, entry by argument
			date = dia.getAttribute("fecha")	
			probPrecip = dia.getElementsByTagName("prob_precipitacion")[0]
			tempMax = dia.getElementsByTagName("maxima")[0]
			tempMin = dia.getElementsByTagName("minima")[0]			
			try:				
				fecha = date
				probabilidad = probPrecip.firstChild.data
				maxima = tempMax.firstChild.data
				minima = tempMin.firstChild.data
				if (fecha==day):
					print("\nfecha: %s | prob general lluvia: %s | temp Max: %s grados | temp Min: %s grados" % (date, probPrecip.firstChild.data, tempMax.firstChild.data, tempMin.firstChild.data))													
			except:
				pass
#End class	
			
