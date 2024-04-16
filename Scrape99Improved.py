from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import time
from typing import List
from pandas import DataFrame, ExcelWriter
from city import city
from store import store
from config import config

edge_options = Options()
edge_options.add_argument("ms:inPrivate")
edge_options.add_argument("headless")
edge_options.add_argument("disable-gpu")
driver = webdriver.Edge(options=edge_options)
stateUrl = "https://locations.99only.com/{state}/"

configuration = config()

states: List[str] = configuration.getStates()
cities: List[city] = list()

for state in states:
    url = stateUrl.format(state = state)
    page = driver.get(url)
    time.sleep(configuration.getBackoff() + configuration.getVariableBackoff())
    elements = driver.find_elements(by=By.CLASS_NAME, value="map-list-item.is-single")
    for elem in elements:
        cities.append(city(elem.text, elem.find_element(by=By.TAG_NAME, value='a').get_attribute("href")))

for c in cities:
    page = driver.get(c.getUrl())
    time.sleep(configuration.getBackoff() + configuration.getVariableBackoff())
    elements = driver.find_elements(by=By.CLASS_NAME, value="map-list-item-wrap.mb-10.loaded")
    idDict = {}
    for e in elements:
        dataID = e.get_attribute('data-lid')
        storeLink = e.find_element(by=By.TAG_NAME, value='a').get_attribute("href")
        address = e.find_element(by=By.CLASS_NAME, value="address").text
        phone = e.find_element(by=By.CLASS_NAME, value="ga-link.phone").text
        name = e.find_element(by=By.CLASS_NAME, value="location-name").text
        idDict[dataID] = (name, phone, storeLink, address)

    mapBlips = driver.find_elements(by=By.CLASS_NAME, value="leaflet-marker-icon.map-marker.cmOverlay.filter-item.leaflet-zoom-animated.leaflet-interactive")
    blipDict = {}
    for blip in mapBlips:
        dataID = blip.get_attribute('data-lid')
        longitude = blip.get_attribute("data-lng")
        latitude = blip.get_attribute("data-lat")
        name, phone, storeLink, address = idDict[dataID]
        c.addStore(store(name=name,phone=phone,address=address,storeUrl=storeLink,latitude=latitude,longitude=longitude))

store_names = []
phone_numbers = []
addresses = []
store_urls = []
latitudes = []
longitudes = []
cityNames = []

for c in cities:
    for s in c.getStores():
        store_names.append(s.getName())
        phone_numbers.append(s.getPhone())
        addresses.append(s.getAddress())
        store_urls.append(s.getUrl())
        latitudes.append(s.getLatitude())
        longitudes.append(s.getLongitude())
        cityNames.append(c.getCityName())

df = DataFrame({'Store Name': store_names, 'Phone Number': phone_numbers, 'Address': addresses, 'Store Url': store_urls, 'Latitude': longitudes, 'Longitude': latitudes, 'City': cityNames})

with ExcelWriter(configuration.getSavePath()) as writer:  
    df.to_excel(writer, sheet_name=configuration.getSheetName(), index=configuration.isIndexed())