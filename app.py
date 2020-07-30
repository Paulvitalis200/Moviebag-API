from flask import Flask, jsonify, request

app = Flask(__name__)

# List of movies
movies = [
    {
        "name": "Shawshank Redemption",
        "casts": ["Tim Robbins", "Morgan Freeman"],
        "genres": ["Drama"]
    },
    {
        "name": "The Godfather",
        "casts": ["Marlon Brando", "Al Pacino"],
        "genres": ["Crime", "Drama"]
    }
]


@app.route('/movies')
def hello():
    return jsonify(movies)


@app.route('/movies', methods=['POST'])
def add_movie():
    movie = request.get_json()
    movies.append(movie)
    return {'id': len(movies)}, 200


@app.route('/movies/<int:index>', methods=['PUT'])
def update_movie(index):
    movie = request.get_json()
    movies[index] = movie
    return jsonify(movies[index]), 200


@app.route('/movies/<int:index>', methods=['DELETE'])
def delete_movie(index):
    movies.pop(index)
    return 'None', 200


app.run()
