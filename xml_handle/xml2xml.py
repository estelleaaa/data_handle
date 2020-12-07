# -*- coding: utf-8 -*-


import os
import os.path
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as ET
from xml.dom import minidom as xml
from xml.dom.minidom import parseString
import shutil


dirRoot = 'test'
for parent, dirnames, filenames in os.walk(dirRoot):
    for filepath in filenames:
        if os.path.splitext(filepath)[1] == '.xml':
            xmlPath = os.path.join(parent,filepath)
            xmlName = os.path.splitext(filepath)
            tree = ET.parse(xmlPath)
            root = tree.getroot()
            for a in root.iter('annotation'):
                a.text = ''
            for o in root.iter('object'):
                o.text = ''
            for poly in root.iter('polygon'):
                poly.text = ''
            for p in root.iter('point'):
                p.text =''
            xml_string = ET.tostring(root)
            xml_write = parseString(xml_string).toprettyxml()
            tree.write('./import/' + os.path.splitext(filepath)[0] + '.xml')
    for file in filenames:
        if os.path.splitext(file)[1] in ('.jpg','.png','.jpeg'):
            shutil.copy(os.path.join(parent, file), os.path.join('import'))
                
        
           
            
            




