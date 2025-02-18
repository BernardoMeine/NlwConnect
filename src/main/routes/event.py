from flask import Blueprint, jsonify, request
from src.http_types.http_response import HttpResponse
from src.http_types.http_request import HttpRequest

event_route_bp = Blueprint('event_route', __name__)

@event_route_bp.route('/event', methods=['POST'])
def create_event():
    return jsonify({"message": "Event created successfully!"}), 201