class store:
    def __init__(self, name, phone, address, storeUrl, latitude, longitude):
        self.name: str = name
        self.phone: str = phone
        self.address: str = address
        self.storeUrl: str = storeUrl
        self.latitude: str = latitude
        self.longitude: str = longitude
    
    def __repr__(self):
        return str({
            "Store Name" : self.name,
            "Phone Number" : self.phone,
            "URL" : self.storeUrl,
            "Address" : self.address,
            "Latitude" : self.latitude,
            "Longitude" : self.longitude
        })
    
    def __str__(self):
        return str({
            "Store Name" : self.name,
            "Phone Number" : self.phone,
            "URL" : self.storeUrl,
            "Address" : self.address,
            "Latitude" : self.latitude,
            "Longitude" : self.longitude
        })
    
    def getName(self):
        return self.name
    
    def getPhone(self):
        return self.phone
    
    def getUrl(self):
        return self.storeUrl
    
    def getAddress(self):
        return self.address
    
    def getLatitude(self):
        return self.latitude
    
    def getLongitude(self):
        return self.longitude
    
    def getAll(self):
        return {
            "Store Name" : self.getName(),
            "Phone Number" : self.getPhone(),
            "URL" : self.getUrl(),
            "Address" : self.getAddress(),
            "Latitude" : self.getLatitude(),
            "Longitude" : self.getLongitude()
        }