from xml.dom.minidom import parseString
import requests
import csv


url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)

doc = parseString(page.content)
# check it works
print (doc.toprettyxml(), end='') #output to console

# if I want to store the xml in a file
with open("trainxml.xml","w") as xmlfp:
    doc.writexml(xmlfp)


url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)

doc = parseString(page.content)
# check it works
print (doc.toprettyxml(), end='') #output to console

# if I want to store the xml in a file
with open("trainxml.xml","w") as xmlfp:
    doc.writexml(xmlfp)