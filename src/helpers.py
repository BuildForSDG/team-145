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
