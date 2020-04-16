from helpers import getDays, getInfectionsByTime, getCurrentlyInfected, getSeverePositiveCases, getAvailableHospitalBeds


data = {
    "region": {
        "name": "Africa",
        "avgAge": 19.7,
        "avgDailyIncomeInUSD": 5,
        "avgDailyIncomePopulation": 0.71
    },
    "periodType": "days",
    "timeToElapse": 58,
    "reportedCases": 674,
    "population": 66622705,
    "totalHospitalBeds": 1380614
}


def estimator(**data):
    days = getDays(data['periodType'], data['timeToElapse'])

    currentlyInfected = getCurrentlyInfected(data['reportedCases'])
    severeCurrentlyInfected = getCurrentlyInfected(data['reportedCases'], True)

    infectionsByRequestedTime = getInfectionsByTime(currentlyInfected, days)
    severeInfectionsByRequestedTime = getInfectionsByTime(
        severeCurrentlyInfected, days)

    severeCasesByRequestedTime = getSeverePositiveCases(
        infectionsByRequestedTime)
    extremeSevereCasesByRequestedTime = getSeverePositiveCases(
        severeInfectionsByRequestedTime)

    hospitalBedsByRequestTime = getAvailableHospitalBeds(
        data['totalHospitalBeds'], severeCasesByRequestedTime)
    severeHospitalBedsByRequestTime = getAvailableHospitalBeds(
        data['totalHospitalBeds'], extremeSevereCasesByRequestedTime)

    impact = {"currentlyInfected": currentlyInfected,
              "infectionsByRequestedTime": infectionsByRequestedTime,
              "severeCasesByRequestedTime": severeCasesByRequestedTime,
              "hospitalBedsByRequestTime": hospitalBedsByRequestTime}
    severeImpact = {"currentlyInfected": severeCurrentlyInfected,
                    "infectionsByRequestedTime": severeInfectionsByRequestedTime,
                    "severeCasesByRequestedTime": extremeSevereCasesByRequestedTime,
                    "hospitalBedsByRequestTime": severeHospitalBedsByRequestTime}
    return {"data": data, "impact": impact, "severeImpact": severeImpact}


print(estimator(**data))
