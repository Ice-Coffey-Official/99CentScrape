import requests
from bs4 import BeautifulSoup as Soup
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time 

edge_options = Options()
edge_options.add_argument("ms:inPrivate")

driver = webdriver.Edge(options=edge_options)

baseUrl = "https://locations.99only.com/?q="
locations = ["Los%20Angeles,%20CA,%20US"]#, "Cupertino,%20CA,%20US"]

locationDict = {}

for location in locations:
    locationDict[location] = tuple()
    completeUrl = baseUrl + location
    print(completeUrl)
    page = driver.get(completeUrl)
    time.sleep(3)
    elements = driver.find_elements(by=By.CLASS_NAME, value="leaflet-marker-icon")
    for e in elements:
        tempList = list(locationDict[location])
        tempList.append((e.get_attribute("data-lng"),e.get_attribute("data-lat")))
        tempTuple = tuple(tempList)
        locationDict[location] = tempTuple
        print(e.get_attribute("data-lng"))
        print(e.get_attribute("data-lat"))
print(locationDict)