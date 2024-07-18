from flask import Blueprint, jsonify

api = Blueprint('api', __name__)

@api.route('/api/map/markers', methods=['GET'])
def get_markers():
    markers = [
        {'position': {'lat': 51.5, 'lng': -0.09}, 'title': 'Marker 1'},
        {'position': {'lat': 51.51, 'lng': -0.1}, 'title': 'Marker 2'},
        {'position': {'lat': 51.49, 'lng': -0.08}, 'title': 'Marker 3'},
    ]
    return jsonify(markers)
