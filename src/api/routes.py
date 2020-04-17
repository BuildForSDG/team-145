import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from estimator import estimator, data
from flask import Flask, make_response, request, jsonify, Response
from dicttoxml import dicttoxml

app = Flask(__name__)


@app.route('/api/v1/covid-19', methods=['POST'])
def default_route():
    results = estimator(**data)
    return jsonify(results)


@app.route('/api/v1/covid-19/json', methods=['POST'])
def json_route():
    results = estimator(**data)
    return jsonify(results)

@app.route('/api/v1/covid-19/xml', methods=['POST'])
def xml_route():
    results = estimator(**data)
    xml = xml = dicttoxml(results, root=False, attr_type=False)
    return Response(xml, mimetype='application/xml')


if __name__ == "__main__":
    app.run(debug=True)
