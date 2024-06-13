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



# CUE start/stop
@app.route('/control/<string:command>/<int:ueId>', methods=['POST'])
def ue_control_start(command, ueId):
    if command not in ['start', 'stop']:
        return bad_request("Invalid command")
    cuecf_data_store.setdefault(ueId, {})['ue_control'] = command
    return jsonify({"result": f"UE control {command} command executed successfully"}), 201

# Get UE Configuration Status
@app.route('/configuration/<int:ueId>', methods=['GET'])
def get_ue_configuration(ueId):
    return jsonify(cuecf_data_store.get(ueId, {}).get('ue_configuration', {})), 200

# UE Reconfiguration
@app.route('/configuration/<int:ueId>', methods=['POST'])
def configure_radio_comms(ueId):
    cuecf_data_store.setdefault(ueId, {})['ue_configuration'] = request.json
    return jsonify({"result": "UE reconfiguration successful"}), 201


if __name__ == '__main__':
    app.run(debug=True)

