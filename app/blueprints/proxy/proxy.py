# # app/blueprints/proxy.py

# from flask import Blueprint, request, jsonify
# import requests
# from flask_cors import cross_origin

# proxy_bp = Blueprint('proxy', __name__)

# @proxy_bp.route('/proxy', methods=['GET'])
# @cross_origin()  # Enable CORS for this route
# def proxy():
#     target_url = request.args.get('url')
#     if not target_url:
#         return jsonify({"error": "URL parameter is missing"}), 400

#     try:
#         response = requests.get(target_url)
#         response.raise_for_status()
#         return jsonify(response.json())
#     except requests.exceptions.RequestException as e:
#         return jsonify({"error": str(e)}), 500
# app/blueprints/proxy.py

from flask import Blueprint, request, jsonify
import requests

proxy_bp = Blueprint('proxy', __name__)

@proxy_bp.route('/proxy', methods=['GET'])
def proxy():
    target_url = request.args.get('url')
    google_maps_api_key = "AIzaSyAPc_6sz46iF_TGER4yAVGtQWIHzNH0ozY"  # Replace with your Google Maps API key

    if not target_url:
        return jsonify({"error": "URL parameter is missing"}), 400

    try:
        # Append the Google Maps API key to the target URL
        full_url = f"{target_url}&key={google_maps_api_key}"

        # Make a GET request to the Google Maps API
        response = requests.get(full_url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Return the JSON response from Google Maps API
        return jsonify(response.json())

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


