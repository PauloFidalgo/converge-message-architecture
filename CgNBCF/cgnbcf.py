from flask import Flask, request, jsonify

app = Flask(__name__)

# Example data store for CgNBCF
cgnbcf_data_store = {
    1 : {
        'gnb_control' : 'stop',
        'gnb_configuration' : '',
        'gnb_telemetry': '',
    }
}

# Error handling
@app.errorhandler(404)
def not_found(error):
    problem = {
        'error' : {
            'type' : "",
            'title' : "Resource Not Found",
            'status' : 404,
            'detail' : "The resource you requested was not found.",
            'instance' : request.url
        }
    }
    return jsonify(problem), 404

@app.errorhandler(400)
def bad_request(error):
    problem = {
        'error' : {
            'type' : "",
            'title' : "Bad Request",
            'status' : 400,
            'detail' : "The request could not be understood or was missing required parameters.",
            'instance' : request.url
        }
    }
    return jsonify(problem), 400

@app.errorhandler(500)
def internal_error(error):
    problem = {
        'error' : {
            'type' : "",
            'title' : "Internal Server Error",
            'status' : 500,
            'detail' : "An unexpected error occurred on the server.",
            'instance' : request.url
        }
    }
    return jsonify(problem), 500



# gNB start/stop
@app.route('/control/<string:command>/<int:gnbId>', methods=['POST'])
def gnb_control_start(command, gnbId):
    if command not in ['start', 'stop']:
        return bad_request("Invalid command")
    cgnbcf_data_store.setdefault(gnbId, {})['gnb_control'] = command
    return jsonify({"result": f"gNB control {command} command executed successfully"}), 201

# Get gNB Configuration Status
@app.route('/configuration/<int:gnbId>', methods=['GET'])
def get_gnb_configuration(gnbId):
    return jsonify(cgnbcf_data_store.get(gnbId, {}).get('gnb_configuration', {})), 200

# gNB Reconfiguration
@app.route('/configuration/<int:gnbId>', methods=['POST'])
def configure_radio_comms(lisId):
    cgnbcf_data_store.setdefault(lisId, {})['gnb_configuration'] = request.json
    return jsonify({"result": "gNB reconfiguration successful"}), 201

# Get gNB Data Collection
@app.route('/telemetry/<int:gnbId>', methods=['GET'])
def get_gnb_configuration(gnbId):
    return jsonify(cgnbcf_data_store.get(gnbId, {}).get('gnb_telemetry', {})), 200


if __name__ == '__main__':
    app.run(debug=True)

