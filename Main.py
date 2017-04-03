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
#trying to create a graphic interface with python
	prueba = ParseXml.ParseXml()	
	prueba.getName()
	prueba.getUrl()
	prueba.printAttributes()
else:
	print "Mala conexión a internet. Contacte con administrador"
