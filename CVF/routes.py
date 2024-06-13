## @package CVCF_API
# Documentation for CVCF API
# This file contains the services made available by CVCF

from flask import Flask, request, jsonify

app = Flask(__name__)

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


## @brief CVCF sends a start/stop command to the cameras
#  @param command The command to execute (start/stop).
#  @param cameraId The ID of the camera.
#  @return JSON response with the result of the command.
@app.route('/control/cameras/<int:cameraId>/<string:command>', methods=['POST'])
def cvf_control_start(command, cameraId):
    if command not in ['start', 'stop']:
        return bad_request("Invalid command")
    cvf_data_store.setdefault(cameraId, {})['cvf_control'] = command
    return jsonify({"result": f"CV control {command} command executed successfully"}), 201

## @brief Set camera configuration based on its ID
#  @param cameraId The ID of the camera.
#  @return JSON response with the result of the configuration.
@app.route('/configuration/cameras/<int:cameraId>', methods=['POST'])
def configure_camera(cameraId):
    cvf_data_store.setdefault(cameraId, {})['camera_configuration'] = request.json
    return jsonify({"result": "Camera reconfiguration successful"}), 201

## @brief Get camera status
#  @param cameraId The ID of the camera.
#  @return JSON response with the current status.
@app.route('/configuration/cameras/<int:cameraId>/status', methods=['GET'])
def get_camera_status(cameraId):
    return jsonify(cvf_data_store.get(cameraId, {}).get('camera_status', {})), 200

## @brief Get camera configuration
#  @param cameraId The ID of the camera.
#  @return JSON response with the current configuration.
@app.route('/configuration/cameras/<int:cameraId>', methods=['GET'])
def get_camera_configuration(cameraId):
    return jsonify(cvf_data_store.get(cameraId, {}).get('camera_configuration', {})), 200

## @brief CVCF sends a start/stop command to activate/deactivate support vision model
#  @param command The command to execute (start/stop).
#  @param modelId The ID of the vision model.
#  @return JSON response with the result of the command.
@app.route('/control/vision-model/<int:modelId>/<string:command>', methods=['POST'])
def visual_model_control_start(command, modelId):
    if command not in ['start', 'stop']:
        return bad_request("Invalid command")
    vm_data_store.setdefault(modelId, {})['vision_model_control'] = command
    return jsonify({"result": f"Vision Model control {command} command executed successfully"}), 201

## @brief Set support vision model configuration based on its ID
#  @param modelId The ID of the vision model.
#  @return JSON response with the result of the configuration.
@app.route('/configuration/vision-model/<int:modelId>', methods=['POST'])
def configure_visual_model(modelId):
    vm_data_store.setdefault(modelId, {})['vision_model_configuration'] = request.json
    return jsonify({"result": "Vision Model reconfiguration successful"}), 201

## @brief Get support vision model configuration
#  @param modelId The ID of the vision model.
#  @return JSON response with the current configuration.
@app.route('/configuration/vision-model/<int:modelId>', methods=['GET'])
def get_vision_model_configuration(modelId):
    return jsonify(vm_data_store.get(modelId, {}).get('vision_model_configuration', {})), 200

## @brief Get support vision model status
#  @param modelId The ID of the vision model.
#  @return JSON response with the current status.
@app.route('/configuration/vision-model/<int:modelId>/status', methods=['GET'])
def get_vision_model_status(modelId):
    return jsonify(vm_data_store.get(modelId, {}).get('vision_model_status', {})), 200


if __name__ == '__main__':
    app.run(debug=True)