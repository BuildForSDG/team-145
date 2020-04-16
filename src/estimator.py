from helpers import getDays, getInfectionsByTime, getCurrentlyInfected, getSeverePositiveCases, getAvailableHospitalBeds, getCasesForICU, getCasesForVentilators, getEconomicImpact


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

    casesForICUByRequestedTime = getCasesForICU(infectionsByRequestedTime)
    severeCasesForICUByRequestedTime = getCasesForICU(
        severeInfectionsByRequestedTime)

    casesForVentilatorsByRequestTime = getCasesForVentilators(
        infectionsByRequestedTime)
    severeCasesForVentilatorsByRequestTime = getCasesForVentilators(
        severeInfectionsByRequestedTime)

    dollarsInFlight = getEconomicImpact(
        infectionsByRequestedTime,
        data['region']['avgDailyIncomePopulation'],
        data['region']['avgDailyIncomeInUSD'],
        days
    )
    severeDollarsInFlight = getEconomicImpact(
        severeInfectionsByRequestedTime,
        data['region']['avgDailyIncomePopulation'],
        data['region']['avgDailyIncomeInUSD'],
        days
    )

    impact = {
        "currentlyInfected": currentlyInfected,
        "infectionsByRequestedTime": infectionsByRequestedTime,
        "severeCasesByRequestedTime": severeCasesByRequestedTime,
        "hospitalBedsByRequestTime": hospitalBedsByRequestTime,
        "casesForICUByRequestedTime": casesForICUByRequestedTime,
        "casesForVentilatorsByRequestTime": casesForVentilatorsByRequestTime,
        "dollarsInflight": dollarsInFlight
    }

    severeImpact = {
        "currentlyInfected": severeCurrentlyInfected,
        "infectionsByRequestedTime": severeInfectionsByRequestedTime,
        "severeCasesByRequestedTime": extremeSevereCasesByRequestedTime,
        "hospitalBedsByRequestTime": severeHospitalBedsByRequestTime,
        "casesForICUByRequestedTime": severeCasesForICUByRequestedTime,
        "casesForVentilatorsByRequestTime": severeCasesForVentilatorsByRequestTime,
        "dollarsInflight": severeDollarsInFlight
    }

    return {"data": data, "impact": impact, "severeImpact": severeImpact}


print(estimator(**data))
