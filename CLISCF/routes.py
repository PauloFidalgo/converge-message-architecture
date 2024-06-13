## @package CLIS_API
#  Documentation for CLIS API
#  This file contains the services made available by CLIS

from flask import Flask, request, jsonify

app = Flask(__name__)

# Example data store for CLISCF
cliscf_data_store = {
    0: {
        'placement_status': 'RUNNING'
    },
    1: {
        'placement_status': 'READY'
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
        'error': {
            'type': "",
            'title': "Resource Not Found",
            'status': 404,
            'detail': "The resource you requested was not found.",
            'instance': request.url
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
        'error': {
            'type': "",
            'title': "Bad Request",
            'status': 400,
            'detail': "The request could not be understood or was missing required parameters.",
            'instance': request.url
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
        'error': {
            'type': "",
            'title': "Internal Server Error",
            'status': 500,
            'detail': "An unexpected error occurred on the server.",
            'instance': request.url
        }
    }
    return jsonify(problem), 500

@app.route('/control/placement/<int:lisId>/<string:command>', methods=['POST'])
def control_placement(command, lisId):
    """
    @brief Sends a Start/Stop command to initiate/stop movement of the LIS.
    @param command The command to execute (start/stop).
    @param lisId The ID of the LIS.
    @return JSON response with the result of the command.
    """
    if command not in ['start', 'stop']:
        return bad_request("Invalid command")
    cliscf_data_store.setdefault(lisId, {})['placement_status'] = command
    return jsonify({"result": f"Placement {command} command executed successfully"}), 201

@app.route('/configuration/placement/<int:lisId>', methods=['POST'])
def configure_placement(lisId):
    """
    @brief Configures the placement position of the LIS.
    @param lisId The ID of the LIS.
    @return JSON response with the result of the configuration.
    """
    cliscf_data_store.setdefault(lisId, {})['placement_configuration'] = request.json
    return jsonify({"result": "Placement configuration successful"}), 201

@app.route('/configuration/placement/<int:lisId>', methods=['GET'])
def get_placement_configuration(lisId):
    """
    @brief Gets the current LIS placement configuration.
    @param lisId The ID of the LIS.
    @return JSON response with the current configuration.
    """
    return jsonify(cliscf_data_store.get(lisId, {}).get('placement_configuration', {})), 200

@app.route('/configuration/placement/<int:lisId>/status', methods=['GET'])
def get_placement_status(lisId):
    """
    @brief Gets the current LIS placement status.
    @param lisId The ID of the LIS.
    @return JSON response with the current status.
    """
    return jsonify(cliscf_data_store.get(lisId, {}).get('placement_status', {})), 200

@app.route('/control/radio-comms/<int:lisId>/<string:command>', methods=['POST'])
def control_radio_comms(command, lisId):
    """
    @brief Sends a Start/Stop command to deploy/reset the configured LIS radio communications.
    @param command The command to execute (start/stop).
    @param lisId The ID of the LIS.
    @return JSON response with the result of the command.
    """
    if command not in ['start', 'stop']:
        return bad_request("Invalid command")
    cliscf_data_store.setdefault(lisId, {})['radio_comms_status'] = command
    return jsonify({"result": f"Radio communications {command} command executed successfully"}), 201

@app.route('/configuration/radio-comms/<int:lisId>', methods=['POST'])
def configure_radio_comms(lisId):
    """
    @brief Configures the LIS radio communications.
    @param lisId The ID of the LIS.
    @return JSON response with the result of the configuration.
    """
    cliscf_data_store.setdefault(lisId, {})['radio_comms_configuration'] = request.json
    return jsonify({"result": "Radio communications configuration successful"}), 201

@app.route('/configuration/radio-comms/<int:lisId>/feedback', methods=['POST'])
def radio_comms_feedback(lisId):
    """
    @brief Enables the provision of feedback in terms of UE received power, to allow for automatic beam calibration.
    @param lisId The ID of the LIS.
    @return JSON response with the result of the feedback.
    """
    cliscf_data_store.setdefault(lisId, {})['radio_comms_feedback'] = request.json
    return jsonify({"result": "Radio communications feedback received"}), 201

@app.route('/configuration/radio-comms/<int:lisId>', methods=['GET'])
def get_radio_comms_configuration(lisId):
    """
    @brief Gets the LIS radio communication configuration.
    @param lisId The ID of the LIS.
    @return JSON response with the current configuration.
    """
    return jsonify(cliscf_data_store.get(lisId, {}).get('radio_comms_configuration', {})), 200

@app.route('/configuration/radio-comms/<int:lisId>/status', methods=['GET'])
def get_radio_comms_status(lisId):
    """
    @brief Gets the LIS radio communication status.
    @param lisId The ID of the LIS.
    @return JSON response with the current status.
    """
    return jsonify(cliscf_data_store.get(lisId, {}).get('radio_comms_status', {})), 200

@app.route('/control/radio-sensing/<int:lisId>/<string:command>', methods=['POST'])
def control_radio_sensing(command, lisId):
    """
    @brief Sends a Start/Stop command to deploy/reset the configured radio sensing setup.
    @param command The command to execute (start/stop).
    @param lisId The ID of the LIS.
    @return JSON response with the result of the command.
    """
    if command not in ['start', 'stop']:
        return bad_request("Invalid command")
    cliscf_data_store.setdefault(lisId, {})['radio_sensing_status'] = command
    return jsonify({"result": f"Radio sensing {command} command executed successfully"}), 201

@app.route('/configuration/radio-sensing/<int:lisId>', methods=['POST'])
def configure_radio_sensing(lisId):
    """
    @brief Configures the LIS radio sensing.
    @param lisId The ID of the LIS.
    @return JSON response with the result of the configuration.
    """
    cliscf_data_store.setdefault(lisId, {})['radio_sensing_configuration'] = request.json
    return jsonify({"result": "Radio sensing configuration successful"}), 201

@app.route('/configuration/radio-sensing/<int:lisId>/status', methods=['GET'])
def get_radio_sensing_status(lisId):
    """
    @brief Gets the LIS radio sensing status.
    @param lisId The ID of the LIS.
    @return JSON response with the current status.
    """
    return jsonify(cliscf_data_store.get(lisId, {}).get('radio_sensing_status', {})), 200

if __name__ == '__main__':
    app.run(debug=True)