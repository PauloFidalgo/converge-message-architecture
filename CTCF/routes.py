## @package CTCF_API
# Documentation for CTCF API
# This file contains the services made available by CTCF

from flask import Flask, request, jsonify

app = Flask(__name__)

# Example data store for CAF
ctcf_data_store = {
    0 : {
        'ctcf_status' : 'OK',
        'traffic_control_rules': 'Ola'
    },
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

## @brief CTCF sends a start/stop command to control traffic servers
#  @param command The command to execute (start/stop).
#  @param ctcfId The ID of the CTCF.
#  @return JSON response with the result of the command.
@app.route('/control/<int:ctcfId>/<string:command>', methods=['POST'])
def traffic_control_start(command, ctcfId):
    if command not in ['start', 'stop']:
        return bad_request("Invalid command")
    ctcf_data_store.setdefault(ctcfId, {})['traffic_control'] = command
    return jsonify({"result": f"Traffic Control {command} command executed successfully"}), 201

## @brief Get the current traffic control rules configuration
#  @param ctcfId The ID of the CTCF.
#  @return JSON response with the current configuration.
@app.route('/configuration/<int:ctcfId>/rules', methods=['GET'])
def get_traffic_control_rules(ctcfId):
    return jsonify(ctcf_data_store.get(ctcfId, {}).get('ctcf_rules', {})), 200

## @brief Add or modify traffic control rules
#  @param ctcfId The ID of the CTCF.
#  @return JSON response with the result of the configuration.
@app.route('/configuration/<int:ctcfId>/rules', methods=['POST'])
def add_traffic_control_rules(ctcfId):
    ctcf_data_store.setdefault(ctcfId, {})['ctcf_rules'] = request.json
    return jsonify({"result": "Traffic Control Rules configuration successful"}), 201

## @brief Get statistics related to traffic control
#  @param ctcfId The ID of the CTCF.
#  @return JSON response with the current statistics.
@app.route('/telemetry/<int:ctcfId>', methods=['GET'])
def get_traffic_statistics(ctcfId):
    return jsonify(ctcf_data_store.get(ctcfId, {}).get('traffic_statistics', {})), 200

if __name__ == '__main__':
    app.run(debug=True)