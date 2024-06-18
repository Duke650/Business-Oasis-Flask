from flask import Flask, request, jsonify
import requests

prox = Flask(__name__)

@prox.route('/proxy')
def proxy():
    target_url = request.args.get('url')
    if not target_url:
        return jsonify({"error": "URL parameter is missing"}), 400

    try:
        response = requests.get(target_url)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

# if __name__ == '__main__':
#     proxy.run(port=5000)
