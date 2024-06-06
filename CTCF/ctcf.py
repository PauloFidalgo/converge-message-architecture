from flask import Flask, request, jsonify
import ProblemDetails

app = Flask(__name__)

# Example data store for CAF
ctcf_data_store = {
        0 : {
        'ctcf_status' : 'OK',
        'traffic_control_rules':'Ola'
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

# CTCF status
@app.route('/configuration/placement/<int:ctcfId>/status', methods=['GET'])
def get_placement_status(ctcfId):
    return jsonify(ctcf_data_store.get(ctcfId, {}).get('ctcf_status', {})), 200

# Traffic Control start/stop
@app.route('/control/{<string:command>}/<int:ctcfId>', methods=['POST'])
def traffic_control_start(command, ctcfId):
    if command not in ['start', 'stop']:
        return bad_request("Invalid command")
    ctcf_data_store.setdefault(ctcfId, {})['traffic_control'] = command
    return jsonify({"result": f"Traffic Control {command} command executed successfully"}), 201

# Get Traffic Control Rules
@app.route('/configuration/<int:ctcfId>/rules', methods=['GET'])
def get_traffic_control_rules(ctcfId):
    return jsonify(ctcf_data_store.get(ctcfId, {}).get('traffic_control_rules', {})), 200

# Add or modify Traffic Control Rules
@app.route('/configuration/<int:ctcfId>/rules', methods=['POST'])
def add_traffic_control_rules(lisId):
    ctcf_data_store.setdefault(lisId, {})['traffic_control_rules'] = request.json
    return jsonify({"result": " Traffic Control Rules configuration successful"}), 201

# Get Traffic Statistics
@app.route('/telemetry/<int:ctcfId>', methods=['GET'])
def get_traffic_statistics(ctcfId):
    return jsonify(ctcf_data_store.get(ctcfId, {}).get('traffic_Statistics', {})), 200

if __name__ == '__main__':
    app.run(debug=True)

