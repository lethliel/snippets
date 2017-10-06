#!/usr/bin/python

import sys
import xml.etree.cElementTree as ET

if len(sys.argv) == 2:
    xmlfile = sys.argv[1]
    print(xmlfile)
else:
    print('Please provide exactoy one xml file')
    exit(1)

xml = ET.ElementTree(file=xmlfile)
collection = xml.getroot()
print(collection.get('matches'))
for elem in collection:
    for subelem in elem.iter():
          strippedText = subelem.text.strip()
          if strippedText != '':
              print(strippedText) 
