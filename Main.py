#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Main.py
#  
#  Copyright 2016 manrique <https:/github.com/luisFcoOrtiz>
#  
import ParseXml

prueba = ParseXml.ParseXml()
prueba.setUrl("http://www.aemet.es/xml/municipios/localidad_18127.xml")
prueba.openUrl()	
if (prueba.checkConnection()==True):	
	print(prueba.getName())
	print(prueba.getUrl())
	prueba.getAllDates()
	print("Introduzca una fecha")
	diaEnConcreto = raw_input()
	prueba.LookForADay(diaEnConcreto)
else:
	print "Mala conexión a internet. Contacte con administrador"
