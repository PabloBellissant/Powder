
#Basic enumeration that tell basic stuff


enum = {
    0 : {"name" : "AIR", "simpleName" : "AIR", "color" : (0,0,0), "isLiquid" : False, "isSolid" : False, "isGaseous" : True, "isPowder" : False, "pressibility" : 1, "density" : 1.3, "defaultTemperature" : 20, "lowTempId" : 0, "idLowTemp": -10, "highTempId" : 0, "idHighTemp" : 90, "tempPressureModifier" : 1, "electricityConductivity" : 0, "heatConductivity" : 0, "liquidity" : 0, "tempNeededToBurn" : 999999999, "pressureNeededToBurn" : 999999999, "afterBurnId" : 0, "burnTime" : 0, "burnForce" : 0},
    1 : {"name" : "WATER", "simpleName" : "WATR", "color" : (3,40,252), "isLiquid" : True, "isSolid" : False, "isGaseous" : False, "isPowder" : False, "pressibility" : 0.05, "density" : 993, "defaultTemperature" : 20, "lowTempId" : 2, "idLowTemp": 0, "highTempId" : 3, "idHighTemp" : 100, "tempPressureModifier" : 1, "electricityConductivity" : 0.4, "heatConductivity" : 0.7, "liquidity" : 1, "tempNeededToBurn" : 150000, "pressureNeededToBurn" : 0, "afterBurnId" : 0, "burnTime" : 0, "burnForce" : 0},
    2 : {"name" : "ICE", "simpleName" : "ICE", "color" : (110,182,255), "isLiquid" : False, "isSolid" : True, "isGaseous" : False, "isPowder" : False, "pressibility" : 0.05, "density" : 917, "defaultTemperature" : -18, "lowTempId" : 0, "idLowTemp": -1000, "highTempId" : 1, "idHighTemp" : 0, "tempPressureModifier" : 1, "electricityConductivity" : 0, "heatConductivity" : 0.4, "liquidity" : 0, "tempNeededToBurn" : 150000, "pressureNeededToBurn" : 0, "afterBurnId" : 0, "burnTime" : 0, "burnForce" : 0},
    3 : {"name" : "STEAM", "simpleName" : "STM", "color" : (108, 124, 140), "isLiquid" : False, "isSolid" : False, "isGaseous" : True, "isPowder" : False, "pressibility" : 0.05, "density" : 0.0006, "defaultTemperature" : 150, "lowTempId" : 1, "idLowTemp": 100, "highTempId" : 0, "idHighTemp" : 999999999999, "tempPressureModifier" : 1, "electricityConductivity" : 0.01, "heatConductivity" : 0.05, "liquidity" : 0, "tempNeededToBurn" : 150000,"pressureNeededToBurn" : 0, "afterBurnId" : 0, "burnTime" : 0, "burnForce" : 0},
    4 : {"name" : "SNOW", "simpleName" : "SNOW", "color" : (245, 245, 255), "isLiquid" : False, "isSolid" : False, "isGaseous" : False, "isPowder" : True, "pressibility" : 0.05, "density" : 500, "defaultTemperature" : -5, "lowTempId" : 2, "idLowTemp": -50, "highTempId" : 1, "idHighTemp" : 0, "tempPressureModifier" : 1, "electricityConductivity" : 0.01, "heatConductivity" : 0.6, "liquidity" : 0.1, "tempNeededToBurn" : 150000,"pressureNeededToBurn" : 0, "afterBurnId" : 0, "burnTime" : 0, "burnForce" : 0},
    5 : {"name" : "ROCK", "simpleName" : "ROCK", "color" : (109, 109, 109), "isLiquid" : False, "isSolid" : True, "isGaseous" : False, "isPowder" : False, "pressibility" : 0.05, "density" : 2700, "defaultTemperature" : 10, "lowTempId" : 1, "idLowTemp": -300, "highTempId" : 7, "idHighTemp" : 2500, "tempPressureModifier" : 1, "electricityConductivity" : 0.01, "heatConductivity" : 0.35, "liquidity" : 0, "tempNeededToBurn" : 15000,"pressureNeededToBurn" : 0, "afterBurnId" : 0, "burnTime" : 0, "burnForce" : 0},
    6 : {"name" : "STONE", "simpleName" : "STN", "color" : (89, 89, 89), "isLiquid" : False, "isSolid" : False, "isGaseous" : False, "isPowder" : True, "pressibility" : 0.05, "density" : 2700, "defaultTemperature" : 20, "lowTempId" : 5, "idLowTemp": -10, "highTempId" : 7, "idHighTemp" : 1500, "tempPressureModifier" : 1, "electricityConductivity" : 0.01, "heatConductivity" : 0.4, "liquidity" : 0, "tempNeededToBurn" : 15000,"pressureNeededToBurn" : 0, "afterBurnId" : 0, "burnTime" : 0, "burnForce" : 0},
    7 : {"name": "LAVA", "simpleName": "LAVA", "color": (214, 102, 4), "isLiquid": True, "isSolid": False,"isGaseous": False, "isPowder": False, "pressibility": 0.05, "density" : 2200, "defaultTemperature" : 2926, "lowTempId": 6, "idLowTemp": 1500, "highTempId": 8,"idHighTemp": 12700, "tempPressureModifier": 1, "electricityConductivity": 0.01, "heatConductivity": 0.7,"liquidity": 0.3, "tempNeededToBurn": 15000, "pressureNeededToBurn": 0, "afterBurnId": 0, "burnTime": 0,"burnForce": 0},
    8 : {"name": "VAPORIZED LAVA", "simpleName": "VLAV", "color": (230, 198, 112), "isLiquid": False, "isSolid": False,"isGaseous": True, "isPowder": False, "pressibility": 0.05, "density" : 0.04, "defaultTemperature" : 150000, "lowTempId": 7, "idLowTemp": 127500, "highTempId": 8,"idHighTemp": 9999999999, "tempPressureModifier": 1, "electricityConductivity": 0.01, "heatConductivity": 0,"liquidity": 0, "tempNeededToBurn": 1500000, "pressureNeededToBurn": 150, "afterBurnId": 0, "burnTime": 10,"burnForce": 1}

}


def getName(id):
    return enum.get(id).get("name")

def getSimpleName(id):
    return enum.get(id).get("simpleName")

def getColor(id):
    return enum.get(id).get("color")

def isLiquid(id):
    return enum.get(id).get("isLiquid")

def isSolid(id):
    return enum.get(id).get("isSolid")

def isGaseous(id):
    return enum.get(id).get("isGaseous")

def isPowder(id):
    return enum.get(id).get("isPowder")

def getPressibility(id):
    return enum.get(id).get("pressibility")

def getLowTempId(id):
    return enum.get(id).get("lowTempId")

def getIdLowTemp(id):
    return enum.get(id).get("idLowTemp")

def getHighTempId(id):
    return enum.get(id).get("highTempId")

def getIdHighTemp(id):
    return enum.get(id).get("idHighTemp")

def tempPressureModifier(id):
    return enum.get(id).get("tempPressureModifier")

def getElectricityConductivity(id):
    return enum.get(id).get("electricityConductivity")

def getHeatConductivity(id):
    return enum.get(id).get("heatConductivity")

def getLiquidity(id):
    return enum.get(id).get("liquidity")

def getTempNeededToBurn(id):
    return enum.get(id).get("tempNeededToBurn")

def getPressureNeededToBurn(id):
    return enum.get(id).get("pressureNeededToBurn")

def getAfterBurnId(id):
    return enum.get(id).get("afterBurnId")

def getBurnTime(id):
    return enum.get(id).get("burnTime")

def getBurnForce(id):
    return enum.get(id).get("burnForce")

def getDefaultTemperature(id):
    return enum.get(id).get("defaultTemperature")

def getDensity(id):
    return enum.get(id).get("density")


