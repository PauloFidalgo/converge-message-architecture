from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Example data stores
gnb_data_store = {
    0 : {
        'placement_status' : 'OK'
    },
    1 : {
        'placement_status' : 'FAILED'
    }
}

ue_data_store = {

}

lis_data_store = {}
ctcf_data_store = {}
simulator_data_store = {}
ml_model_store = {}
odr_dataset_store = {}
experiment_status_store = {}

CLISCF_API_BASE_URL = "http://localhost:5001"

# Error handling
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad request"}), 400

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

def forward_to_cliscf(endpoint, method, data=None):
    url = f"{CLISCF_API_BASE_URL}{endpoint}"
    try:
        if method == 'GET':
            response = requests.get(url)
        elif method == 'POST':
            response = requests.post(url, json=data)
        elif method == 'PUT':
            response = requests.put(url, json=data)
        elif method == 'DELETE':
            response = requests.delete(url)
        else:
            return jsonify({"error": "Unsupported method"}), 405

        response.raise_for_status()  
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


# gNB Endpoints
@app.route('/api/v1/gNB/placement-status/{<int:gnbId>}', methods=['GET'])
def get_gnb_placement_status(gnbId):
    return jsonify(gnb_data_store.get(gnbId, {}).get('placement_status', {})), 200

@app.route('/api/v1/gNB/placement-setup/{<int:gnbId>}', methods=['POST'])
def setup_gnb_placement(gnbId):
    gnb_data_store.setdefault(gnbId, {})['placement_status'] = request.json
    return jsonify({"result": "gNB placement setup successful"}), 201

@app.route('/api/v1/gNB/radiocommunications-status/{<int:gnbId>}', methods=['GET'])
def get_gnb_radio_communications_status(gnbId):
    return jsonify(gnb_data_store.get(gnbId, {}).get('radio_communications_status', {})), 200

@app.route('/api/v1/gNB/radiocommunications-setup/{<int:gnbId>}', methods=['POST'])
def setup_gnb_radio_communications(gnbId):
    gnb_data_store.setdefault(gnbId, {})['radio_communications_status'] = request.json
    return jsonify({"result": "gNB radio communications setup successful"}), 201

@app.route('/api/v1/gNB/radiosensing-status/{<int:gnbId>}', methods=['GET'])
def get_gnb_radio_sensing_status(gnbId):
    return jsonify(gnb_data_store.get(gnbId, {}).get('radio_sensing_status', {})), 200

@app.route('/api/v1/gNB/radiosensing-setup/{<int:gnbId>}', methods=['POST'])
def setup_gnb_radio_sensing(gnbId):
    gnb_data_store.setdefault(gnbId, {})['radio_sensing_status'] = request.json
    return jsonify({"result": "gNB radio sensing setup successful"}), 201

@app.route('/api/v1/gNB/videosensing-status/<int:gnbId>', methods=['GET'])
def get_gnb_video_sensing_status(gnbId):
    return jsonify(gnb_data_store.get(gnbId, {}).get('video_sensing_status', {})), 200

@app.route('/api/v1/gNB/videosensing-setup/{<int:gnbId>}', methods=['POST'])
def setup_gnb_video_sensing(gnbId):
    gnb_data_store.setdefault(gnbId, {})['video_sensing_status'] = request.json
    return jsonify({"result": "gNB video sensing setup successful"}), 201

@app.route('/api/v1/gNB/xapp-status/{<int:id>}', methods=['GET'])
def get_gnb_xapp_status(id):
    return jsonify(gnb_data_store.get(id, {}).get('xapp_status', {})), 200

@app.route('/api/v1/gNB/xapp-setup/<int:id>', methods=['POST'])
def upload_gnb_xapp(id):
    gnb_data_store.setdefault(id, {})['xapp_status'] = request.json
    return jsonify({"result": "gNB x-APP upload successful"}), 201

# UE Endpoints
@app.route('/api/v1/UE/placement-status/{<int:ueId>}', methods=['GET'])
def get_ue_placement_status(ueId):
    return jsonify(ue_data_store.get(ueId, {}).get('placement_status', {})), 200

@app.route('/api/v1/UE/placement-setup/{<int:ueId>}', methods=['POST'])
def setup_ue_placement(ueId):
    ue_data_store.setdefault(ueId, {})['placement_status'] = request.json
    return jsonify({"result": "UE placement setup successful"}), 201

@app.route('/api/v1/UE/radiocommunications-status/{<int:ueId>}', methods=['GET'])
def get_ue_radio_communications_status(ueId):
    return jsonify(ue_data_store.get(ueId, {}).get('radio_communications_status', {})), 200

@app.route('/api/v1/UE/radiocommunications-setup/{<int:ueId>}', methods=['POST'])
def setup_ue_radio_communications(ueId):
    ue_data_store.setdefault(ueId, {})['radio_communications_status'] = request.json
    return jsonify({"result": "UE radio communications setup successful"}), 201

@app.route('/api/v1/UE/radiosensing-status/{<int:ueId>}', methods=['GET'])
def get_ue_radio_sensing_status(ueId):
    return jsonify(ue_data_store.get(ueId, {}).get('radio_sensing_status', {})), 200

@app.route('/api/v1/UE/radiosensing-setup/{<int:ueId>}', methods=['POST'])
def setup_ue_radio_sensing(ueId):
    ue_data_store.setdefault(ueId, {})['radio_sensing_status'] = request.json
    return jsonify({"result": "UE radio sensing setup successful"}), 201

@app.route('/api/v1/UE/videosensing-status/{<int:ueId>}', methods=['GET'])
def get_ue_video_sensing_status(ueId):
    return jsonify(ue_data_store.get(ueId, {}).get('video_sensing_status', {})), 200

@app.route('/api/v1/UE/videosensing-setup/{<int:ueId>}', methods=['POST'])
def setup_ue_video_sensing(ueId):
    ue_data_store.setdefault(ueId, {})['video_sensing_status'] = request.json
    return jsonify({"result": "UE video sensing setup successful"}), 201

# LIS Endpoints
@app.route('/api/v1/LIS/placement-status/{<int:lisId>}', methods=['GET'])
def get_lis_placement_status(lisId):
    return forward_to_cliscf(f"/configuration/placement/{lisId}/status", 'GET')

@app.route('/api/v1/LIS/placement-setup/{<int:lisId>}', methods=['POST'])
def setup_lis_placement(lisId):
    return forward_to_cliscf(f"/configuration/placement/{lisId}", 'POST', request.json)

@app.route('/api/v1/LIS/radiocommunications-status/{<int:lisId>}', methods=['GET'])
def get_lis_radio_communications_status(lisId):
    return forward_to_cliscf(f"/configuration/radio-comms/{lisId}/status", 'GET')

@app.route('/api/v1/LIS/radiocommunications-setup/{<int:lisId>}', methods=['POST'])
def setup_lis_radio_communications(lisId):
    return forward_to_cliscf(f"/configuration/radio-comms/{lisId}", 'POST', request.json)

@app.route('/api/v1/LIS/radiosensing-status/{<int:lisId>}', methods=['GET'])
def get_lis_radio_sensing_status(lisId):
    return forward_to_cliscf(f"/configuration/radio-sensing/{lisId}/status", 'GET')

@app.route('/api/v1/LIS/radiosensing-setup/{<int:lisId>}', methods=['POST'])
def setup_lis_radio_sensing(lisId):
    return forward_to_cliscf(f"/configuration/radio-sensing/{lisId}", 'POST', request.json)

@app.route('/api/v1/LIS/videosensing-status/{<int:lisId>}', methods=['GET'])
def get_lis_video_sensing_status(lisId):
    return forward_to_cliscf(f"/configuration/video-sensing/{lisId}/status", 'GET')

@app.route('/api/v1/LIS/videosensing-setup/{<int:lisId>}', methods=['POST'])
def setup_lis_video_sensing(lisId):
    return forward_to_cliscf(f"/configuration/video-sensing/{lisId}", 'POST', request.json)

# CTCF Endpoints
@app.route('/api/v1/CTCF/status/{<int:ctcfId>}', methods=['GET'])
def get_ctcf_status(ctcfId):
    return jsonify(ctcf_data_store.get(ctcfId, {}).get('status', {})), 200

@app.route('/api/v1/CTCF/setup/{<int:ctcfId>}', methods=['POST'])
def setup_ctcf(ctcfId):
    ctcf_data_store.setdefault(ctcfId, {})['status'] = request.json
    return jsonify({"result": "CTCF setup successful"}), 201

@app.route('/api/v1/CTCF/control/<string:action>/{<int:ctcfId>}', methods=['POST'])
def control_ctcf(action, ctcfId):
    if action not in ['start', 'stop']:
        return bad_request(400)
    ctcf_data_store.setdefault(ctcfId, {})['control'] = action
    return jsonify({"result": f"CTCF {action} command successful"}), 200

@app.route('/api/v1/CTCF/configuration/{<int:ctcfId>}/rules', methods=['GET'])
def get_ctcf_rules(ctcfId):
    return jsonify(ctcf_data_store.get(ctcfId, {}).get('rules', {})), 200

@app.route('/api/v1/CTCF/configuration/{<int:ctcfId>}/rules', methods=['POST'])
def setup_ctcf_rules(ctcfId):
    ctcf_data_store.setdefault(ctcfId, {})['rules'] = request.json
    return jsonify({"result": "CTCF rules setup successful"}), 201

@app.route('/api/v1/CTCF/telemetry/{<int:ctcfId>}', methods=['GET'])
def get_ctcf_telemetry(ctcfId):
    return jsonify(ctcf_data_store.get(ctcfId, {}).get('telemetry', {})), 200

# NET-S Endpoints
@app.route('/api/v1/NETS/status', methods=['GET'])
def get_nets_status():
    return jsonify({"status": "NET-S operational"}), 200

@app.route('/api/v1/NETS/setup', methods=['POST'])
def setup_nets():
    return jsonify({"result": "NET-S setup successful"}), 201

# ML Model Endpoints
@app.route('/api/v1/ML/upload', methods=['POST'])
def upload_ml_model():
    ml_model_store['model'] = request.json
    return jsonify({"result": "ML model upload successful"}), 201

@app.route('/api/v1/ML/download', methods=['GET'])
def download_ml_model():
    return jsonify(ml_model_store.get('model', {})), 200

# ODR Dataset Endpoints
@app.route('/api/v1/ODR/downlink', methods=['GET'])
def download_odr_dataset():
    return jsonify(odr_dataset_store.get('dataset', {})), 200

@app.route('/api/v1/ODR/upload', methods=['POST'])
def upload_odr_dataset():
    odr_dataset_store['dataset'] = request.json
    return jsonify({"result": "ODR dataset upload successful"}), 201

# Experiment Status Endpoint
@app.route('/api/v1/CBF/status', methods=['GET'])
def get_experiment_status():
    return jsonify(experiment_status_store.get('status', {})), 200

if __name__ == '__main__':
    app.run(debug=True)