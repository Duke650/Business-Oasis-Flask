from . import reviews
from flask import request, jsonify
from app.models import Review


@reviews.route("/create_review", methods=["POST"])
def createReview():
    data = request.json
    print(data)
    new_review = Review(
        title = data["review"]['title'],
        body = data["review"]['body'],
        client_first_name = data["review"]['client_first_name'],
        client_last_name = data["review"]['client_last_name'],
        rating = data["review"]['rating'],
        date = data["review"]['date'],
        user_id=data["review"]["user_id"],
        job_location_id = data["review"]["job_location_id"]
    )
    new_review.save()
    return jsonify({"Message": "Review successfully created!"})

@reviews.route("/get_reviews_by_location_id/<id>")
def get_reviews_by_location_id(id):
    all_reviews = Review.query.filter_by(job_location_id = id).all()
    reviews_list = []
    for review in all_reviews:
        reviews_list.append({
            "id": review.id,
            "title": review.title,
            "body": review.body,
            "client_first_name": review.client_first_name,
            "client_last_name": review.client_last_name,
            "rating": review.rating,
            "date": review.date
        })
        print(reviews_list)
    return jsonify({"reviews": reviews_list})