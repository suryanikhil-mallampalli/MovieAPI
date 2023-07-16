from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
VALID_API_KEY = "260cdb2f0b9569143a580580c4deb0b6"
MOVIE_API_BASE_URL = "https://api.tmdb.org/3/"

def validate_api_key(api_key):
    # Function to validate the API key provided by the user
    return api_key == VALID_API_KEY

@app.before_request
def authenticate_request():
    # This function is executed before every request is processed.
    # It checks the API key provided in the query parameters and ensures it is valid.
    api_key = request.args.get("api_key")
    if not api_key or not validate_api_key(api_key):
        # If the API key is missing or invalid, return a JSON response with an error message and 401 status code.
        return jsonify({"error": "Invalid API key"}), 401

@app.route("/movies/<string:movie_name>", methods=["GET"])
def get_movie_details(movie_name):
    # This route is used to fetch details of a specific movie by its name.
    # It expects the movie name as a URL parameter.
    api_key = request.args.get("api_key")
    response = requests.get(f"{MOVIE_API_BASE_URL}search/movie", params={"api_key": api_key, "query": movie_name})
    data = response.json()
    if "results" in data and len(data["results"]) > 0:
        # If the search result contains movie data, return the details of the first movie as a JSON response.
        movie = data["results"][0]
        return jsonify(movie)

    # If the movie is not found, return a JSON response with an error message and 404 status code.
    return jsonify({"error": "Movie not found"}), 404

@app.route("/movies", methods=["GET"])
def get_all_movies():
    # This route is used to fetch a list of all available movies.
    # It does not require any additional parameters.
    api_key = request.args.get("api_key")
    response = requests.get(f"{MOVIE_API_BASE_URL}discover/movie", params={"api_key": api_key})
    data = response.json()
    if "results" in data:
        # If the API response contains a list of movies, return it as a JSON response.
        return jsonify(data["results"])

    # If no movies are found, return a JSON response with an error message and 404 status code.
    return jsonify({"error": "No movies found"}), 404

if __name__ == "__main__":
    # Start the Flask app in debug mode.
    app.run(debug=True)
