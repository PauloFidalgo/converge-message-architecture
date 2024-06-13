## @package CVCF_API
# Documentation for CVCF API
# This file contains the services made available by CVCF

from flask import Flask, request, jsonify

app = Flask(__name__)

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


## CVCF Cameras Start/Stop
# CVCF sends a start/stop command to the cameras
@app.route('/control/cameras/<int:cameraId>/<string:command>', methods=['POST'])
def cvf_control_start(command, cameraId):
    if command not in ['start', 'stop']:
        return bad_request("Invalid command")
    cvf_data_store.setdefault(cameraId, {})['cvf_control'] = command
    return jsonify({"result": f"CV control {command} command executed successfully"}), 201

## CVCF Camera Configuration
# Set camera configuration based on its ID
@app.route('/configuration/cameras/<int:cameraId>', methods=['POST'])
def configure_camera(cameraId):
    cvf_data_store.setdefault(cameraId, {})['camera_configuration'] = request.json
    return jsonify({"result": "Camera reconfiguration successful"}), 201

## CVCF Camera Status
# Get camera status
@app.route('/configuration/cameras/<int:cameraId>/status', methods=['GET'])
def get_camera_status(cameraId):
    return jsonify(cvf_data_store.get(cameraId, {}).get('camera_status', {})), 200

## CVCF Camera Configuration
# Get camera configuration
@app.route('/configuration/cameras/<int:cameraId>', methods=['GET'])
def get_camera_status(cameraId):
    return jsonify(cvf_data_store.get(cameraId, {}).get('camera_configuration', {})), 200

## CVCF Support Vision Models Start/Stop
# CVCF sends a start/stop command to activate/deactivate support vision model
@app.route('/control/vision-model/<int:modelId>/<string:command>', methods=['POST'])
def visual_model_control_start(command, modelId):
    if command not in ['start', 'stop']:
        return bad_request("Invalid command")
    vm_data_store.setdefault(modelId, {})['vision_model_control'] = command
    return jsonify({"result": f"Vision Model control {command} command executed successfully"}), 201

## CVCF Support Vision Models Configuration
# Set support vision model configuration based on its ID
@app.route('/configuration/vision-model/<int:modelId>', methods=['POST'])
def configure_visual_model(modelId):
    vm_data_store.setdefault(modelId, {})['vision_model_configuration'] = request.json
    return jsonify({"result": "Vision Model reconfiguration successful"}), 201

## CVCF Support Vision Models Configuration
# Get support vision model configuration
@app.route('/configuration/vision-model/<int:modelId>', methods=['GET'])
def get_vision_model_status(modelId):
    return jsonify(vm_data_store.get(modelId, {}).get('vision_model_configuration', {})), 200

## CVCF Support Vision Models Status
# Get support vision model status
@app.route('/configuration/vision-model/<int:modelId>/status', methods=['GET'])
def get_vision_model_status(modelId):
    return jsonify(vm_data_store.get(modelId, {}).get('vision_model_status', {})), 200


if __name__ == '__main__':
    app.run(debug=True)

