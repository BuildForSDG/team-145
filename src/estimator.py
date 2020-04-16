from helpers import getDays, getInfectionsByTime, getCurrentlyInfected


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

    impact = {"currentlyInfected": currentlyInfected,
              "infectionsByRequestedTime": infectionsByRequestedTime}
    severeImpact = {"currentlyInfected": severeCurrentlyInfected,
                    "infectionsByRequestedTime": severeInfectionsByRequestedTime}
    return {"data": data, "impact": impact, "severeImpact": severeImpact}


print(estimator(**data))
