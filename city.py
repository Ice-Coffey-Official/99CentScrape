from store import store
from typing import List

class city:
    def __init__(self, name, url):
        self.name: str = name
        self.url: str = url
        self.stores: List[store] = list()
    
    def __repr__(self):
        return str({
            "City Name" : self.name,
            "URL" : self.url,
            "Stores" : self.stores
        })
    
    def __str__(self):
        return str({
            "city Name" : self.name,
            "URL" : self.url,
            "Stores" : self.stores
        })
    
    def addStore(self, store):
        self.stores.append(store)

    def getStores(self):
        return self.stores
    
    def getUrl(self):
        return self.url
    
    def getCityName(self):
        return self.name