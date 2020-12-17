class ControlVirus:
    def __init__(self):
        self.vaccine = [['백신1', 25], ['백신2', 50], ['백신3', 100]]
        self.country = [['한국', 1500, 300], ['중국', 3000, 800], ['일본', 2000, 500],
               ['미국', 2500, 750], ['독일', 2200, 1000]]
        self.increasingInfected = 0
        self.cured = 0
        self.completelyCured = 0
        self.curedCountry = ["" for i in range(5)]

    def getVaccine(self):
        return self.vaccine

    def getCountry(self):
        return self.country

    def getIncreasingInfected(self):
        return self.increasingInfected

    def getCured(self):
        return self.cured

    def getCompletelyCured(self):
        return self.completelyCured

    def getCuredCountry(self):
        return self.curedCountry

    def setVaccine(self, vaccine):
        self.vaccine = vaccine

    def setCountry(self, country):
        self.country = country

    def setIncreasingInfected(self, IncreasingInfected):
        self.increasingInfected  = IncreasingInfected

    def setCured(self, cured):
        self.cured = cured

    def setCuredCountry(self, curedCountry):
        self.curedCountry = curedCountry

    def setCompletelyCured(self, completelyCured):
        self.completelyCured = completelyCured


