import math


def getDays(duration, figure):
    """returns days"""
    if duration == "month":
        return figure*30
    elif duration == "weeks":
        return figure*7
    else:
        return figure


def getInfectionsByTime(currentlyInfected, time):
    numberOfSets = math.trunc(time/3)
    return currentlyInfected*2**numberOfSets


def getCurrentlyInfected(reportedCases, isSevere=False):
    estimated = 50 if isSevere else 10
    return reportedCases*estimated


def getPercentage(figure, quotient):
    """returns percentage point"""
    return figure * quotient


def getSeverePositiveCases(infections):
    return math.trunc(getPercentage(infections, 0.15))


def getAvailableHospitalBeds(capacity, cases):
    availableBeds = getPercentage(capacity, 0.35)
    return math.trunc(availableBeds-cases)


def getCasesForICU(infections):
    return math.trunc(getPercentage(infections, 0.05))


def getCasesForVentilators(infections):
    return math.trunc(getPercentage(infections, 0.02))


def getEconomicImpact(infections, workingPopulation, dailyIncome, period):
    result = (infections*workingPopulation*dailyIncome)/period
    return math.trunc(result)
