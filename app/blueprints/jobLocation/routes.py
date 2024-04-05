from . import jobLocation
from flask import request, jsonify
from app.models import JobLocation


@jobLocation.route('/add_job_location', methods=["POST"])
def createJobLocation():
    data = request.json
    print("DATA ====>", data)

    check_if_location_exists = JobLocation.query.filter_by(
        formatted_address = data['formatted_address']
    ).first()

    if check_if_location_exists:
        return jsonify({"message": "Job Location already exists"})

    new_job_location = JobLocation(
        formatted_address = data['formatted_address']
    )

    new_job_location.save()

    return jsonify({"message": "Job location successfully added"})

@jobLocation.route('/location_by_address/<address>')
def getLocationByAddress(address):
    checkAddress = JobLocation.query.filter_by(formatted_address=address).first()
    print(checkAddress)
    if checkAddress is not None:
        return jsonify({"id": checkAddress.id})
    else:
        return jsonify({"message": "Location doesnt exist"})