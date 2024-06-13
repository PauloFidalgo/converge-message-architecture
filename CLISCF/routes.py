## @package CLIS_API
# Documentation for CLIS API
# This file contains the services made available by CLIS

from flask import Flask, request, jsonify

app = Flask(__name__)

# Example data store for CLISCF
cliscf_data_store = {
    0 : {
        'placement_status' : 'RUNNING'
    },
    1 : {
        'placement_status' : 'READY'
    },
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

## CLIS Placement Start/Stop
# CLIS sends a Start/Stop command to initiate/stop movement of the LIS
@app.route('/control/placement/<int:lisId>/<string:command>', methods=['POST'])
def control_placement(command, lisId):
    if command not in ['start', 'stop']:
        return bad_request("Invalid command")
    cliscf_data_store.setdefault(lisId, {})['placement_status'] = command
    return jsonify({"result": f"Placement {command} command executed successfully"}), 201

## CLIS Placement Configuration
# Configures the placement position of the LIS
@app.route('/configuration/placement/<int:lisId>', methods=['POST'])
def configure_placement(lisId):
    cliscf_data_store.setdefault(lisId, {})['placement_configuration'] = request.json
    return jsonify({"result": "Placement configuration successful"}), 201

## CLIS Placement Configuration 
# Get the current LIS placement configuration
@app.route('/configuration/placement/<int:lisId>', methods=['GET'])
def get_placement_status(lisId):
    return jsonify(cliscf_data_store.get(lisId, {}).get('placement_configuration', {})), 200


## CLIS Placement Status
# Get the current LIS placement status
@app.route('/configuration/placement/<int:lisId>/status', methods=['GET'])
def get_placement_status(lisId):
    return jsonify(cliscf_data_store.get(lisId, {}).get('placement_status', {})), 200

## CLIS Radio Communications Start/Stop
# CLIS sends a Start/Stop command to deploy/reset the configured LIS radio communications
@app.route('/control/radio-comms/<int:lisId>/<string:command>', methods=['POST'])
def control_radio_comms(command, lisId):
    if command not in ['start', 'stop']:
        return bad_request("Invalid command")
    cliscf_data_store.setdefault(lisId, {})['radio_comms_status'] = command
    return jsonify({"result": f"Radio communications {command} command executed successfully"}), 201

## CLIS Radio Communications Configuration
# Configures the LIS radio communications
@app.route('/configuration/radio-comms/<int:lisId>', methods=['POST'])
def configure_radio_comms(lisId):
    cliscf_data_store.setdefault(lisId, {})['radio_comms_configuration'] = request.json
    return jsonify({"result": "Radio communications configuration successful"}), 201

## CLIS Radio Communications Feedback
# Enables the provision of feedback in terms of UE received power, to allow for automatic beam calibration
@app.route('/configuration/radio-comms/<int:lisId>/feedback', methods=['POST'])
def radio_comms_feedback(lisId):
    cliscf_data_store.setdefault(lisId, {})['radio_comms_feedback'] = request.json
    return jsonify({"result": "Radio communications feedback received"}), 201

## CLIS Radio Communications Configuration
# Get the LIS radio communication configuration
@app.route('/configuration/radio-comms/<int:lisId>', methods=['GET'])
def get_radio_comms_status(lisId):
    return jsonify(cliscf_data_store.get(lisId, {}).get('radio_comms_configuration', {})), 200

## CLIS Radio Communications Status
# Get the LIS radio communication status
@app.route('/configuration/radio-comms/<int:lisId>/status', methods=['GET'])
def get_radio_comms_status(lisId):
    return jsonify(cliscf_data_store.get(lisId, {}).get('radio_comms_status', {})), 200

## CLIS Radio Sensing Start/Stop
# CLIS sends a Start/Stop command to deploy/reset the configured radio sensing setup
@app.route('/control/radio-sensing/<int:lisId>/<string:command>', methods=['POST'])
def control_radio_sensing(command, lisId):
    if command not in ['start', 'stop']:
        return bad_request("Invalid command")
    cliscf_data_store.setdefault(lisId, {})['radio_sensing_status'] = command
    return jsonify({"result": f"Radio sensing {command} command executed successfully"}), 201

## CLIS Radio Sensing Configuration
# Configures the LIS radio sensing
@app.route('/configuration/radio-sensing/<int:lisId>', methods=['POST'])
def configure_radio_sensing(lisId):
    cliscf_data_store.setdefault(lisId, {})['radio_sensing_configuration'] = request.json
    return jsonify({"result": "Radio sensing configuration successful"}), 201

## CLIS Radio Sensing Status
# Get the LIS radio sensing status
@app.route('/configuration/radio-sensing/<int:lisId>/status', methods=['GET'])
def get_radio_sensing_status(lisId):
    return jsonify(cliscf_data_store.get(lisId, {}).get('radio_sensing_status', {})), 200

if __name__ == '__main__':
    app.run(debug=True)