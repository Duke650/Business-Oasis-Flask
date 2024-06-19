from flask import Blueprint, request, jsonify
import requests
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

proxy_bp = Blueprint('proxy', __name__)

@proxy_bp.route('/proxy', methods=['GET'])
def proxy():
    target_url = request.args.get('url')
    google_maps_api_key = "AIzaSyAPc_6sz46iF_TGER4yAVGtQWIHzNH0ozY"  # Replace with your Google Maps API key

    if not target_url:
        logging.error("URL parameter is missing")
        return jsonify({"error": "URL parameter is missing"}), 400

    try:
        # Append the Google Maps API key to the target URL
        full_url = f"{target_url}&key={google_maps_api_key}"
        logging.info(f"Requesting URL: {full_url}")

        # Make a GET request to the Google Maps API
        response = requests.get(full_url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Log the status and response
        logging.info(f"Response status: {response.status_code}")
        logging.info(f"Response data: {response.json()}")

        # Return the JSON response from Google Maps API
        return jsonify(response.json())

    except requests.exceptions.RequestException as e:
        logging.error(f"Error during request: {e}")
        return jsonify({"error": str(e)}), 500



