## @package CgNBCF_API
# Documentation for CgNBCF API
# This file contains the services made available by CgNBCF

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
    """
    @brief Handles 404 errors.
    @param error The error object.
    @return JSON response with error details.
    """
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
    """
    @brief Handles 400 errors.
    @param error The error object.
    @return JSON response with error details.
    """
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
    """
    @brief Handles 500 errors.
    @param error The error object.
    @return JSON response with error details.
    """
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


## CgNB Start/Stop
# CgNB sends Start/Stop command to NT-RIC, O-CU, O-DU and O-RU
@app.route('/control/<int:gnbId>/<string:command>', methods=['POST'])
def gnb_control_start(command, gnbId):
    """
    @brief Sends start/stop command to NT-RIC, O-CU, O-DU, and O-RU.
    @param command The command to execute (start/stop).
    @param gnbId The ID of the gNB.
    @return JSON response with the result of the command.
    """
    if command not in ['start', 'stop']:
        return bad_request("Invalid command")
    cgnbcf_data_store.setdefault(gnbId, {})['gnb_control'] = command
    return jsonify({"result": f"gNB control {command} command executed successfully"}), 201

## CgNB Configuration Status
# Get the current CgNB configuration
@app.route('/configuration/<int:gnbId>', methods=['GET'])
def get_gnb_configuration(gnbId):
    """
    @brief Gets the current CgNB configuration.
    @param gnbId The ID of the gNB.
    @return JSON response with the current configuration.
    """
    return jsonify(cgnbcf_data_store.get(gnbId, {}).get('gnb_configuration', {})), 200

## CgNB Status
# Get the current CgNB status
@app.route('/configuration/<int:gnbId>/status', methods=['GET'])
def get_gnb_status(gnbId):
    """
    @brief Gets the current CgNB status.
    @param gnbId The ID of the gNB.
    @return JSON response with the current status.
    """
    return jsonify(cgnbcf_data_store.get(gnbId, {}).get('gnb_status', {})), 200

## CgNB Reconfiguration
# CgNB creates and sends a reconfiguration command via CgNB interface to O-CU, O-DU, O-RU and NT-RIC
@app.route('/configuration/<int:gnbId>', methods=['POST'])
def configure_radio_comms(gnbId):
    """
    @brief Creates and sends a reconfiguration command via CgNB interface to O-CU, O-DU, O-RU, and NT-RIC.
    @param gnbId The ID of the gNB.
    @return JSON response with the result of the reconfiguration.
    """
    cgnbcf_data_store.setdefault(gnbId, {})['gnb_configuration'] = request.json
    return jsonify({"result": "gNB reconfiguration successful"}), 201


if __name__ == '__main__':
    app.run(debug=True)