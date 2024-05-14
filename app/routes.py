from flask import jsonify, request
from app import app

ratings = {}

@app.route('/ratings', methods=['GET'])
def get_ratings():
    return jsonify(ratings)

@app.route('/ratings', methods=['POST'])
def add_rating():
    data = request.get_json()
    user_id = data['user_id']
    rating = data['rating']
    ratings[user_id] = rating
    return jsonify({'message': 'Rating added successfully'})

@app.route('/ratings/average', methods=['GET'])
def get_average_rating():
    if not ratings:
        return jsonify({'message': 'No ratings yet'})
    total_ratings = sum(ratings.values())
    average_rating = total_ratings / len(ratings)
    return jsonify({'average_rating': average_rating})
