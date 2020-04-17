import sys
import os.path
import time
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from dicttoxml import dicttoxml
from flask import Flask, request, g, jsonify, Response
from estimator import estimator, data


app = Flask(__name__)


@app.route('/api/v1/on-covid-19', methods=['POST'])
def default_route():
    results = estimator(**data)
    return jsonify(results)


@app.route('/api/v1/on-covid-19/json', methods=['POST'])
def json_route():
    results = estimator(**data)
    return jsonify(results)


@app.route('/api/v1/on-covid-19/xml', methods=['POST'])
def xml_route():
    results = estimator(**data)
    xml = xml = dicttoxml(results, root=False, attr_type=False)
    return Response(xml, mimetype='application/xml')


@app.route('/api/v1/on-covid-19/logs', methods=['GET'])
def logger():
    f = open("logs.log", "r").read()
    return Response(f, mimetype="text/plain")


@app.before_request
def startTimer():
    g.start = int(round(time.time()*1000))


@app.after_request
def requestLogger(response):
    now = int(round(time.time()*1000))
    duration = now-g.start
    if duration < 10 and duration > 0:
        duration = "0"+str(duration)
    method = request.method
    responseCode = response.status_code
    requestUrl = request.path

    with open("logs.log", "a+") as f:
        f.write(f"{method}\t\t{requestUrl}\t\t{responseCode}\t\t{duration}ms\n")
        f.close()
    return response


if __name__ == "__main__":
    app.run(debug=True)
