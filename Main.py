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
print prueba.getName()
print prueba.getUrl()
prueba.printAttributes()
