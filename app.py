from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)
VALID_API_KEY = "260cdb2f0b9569143a580580c4deb0b6"
MOVIE_API_BASE_URL = "https://api.tmdb.org/3/"

def validate_api_key(api_key):
    return api_key == VALID_API_KEY

@app.before_request
def authenticate_request():
    api_key = request.args.get("api_key")
    if not api_key or not validate_api_key(api_key):
        return jsonify({"error": "Invalid API key"}), 401



#1st version
# # for a certain movie
# @app.route("/movies/<string:movie_name>", methods=["GET"])
# def get_movie_details(movie_name):
#     api_key = request.args.get("api_key")
#     response = requests.get(f"{MOVIE_API_BASE_URL}search/movie", params={"api_key": api_key, "query": movie_name})
#     data = response.json()
#     if "results" in data:
#         if len(data["results"]) > 0:
#             movie = data["results"][0]
#             movie_details = {
#                 "title": movie["title"],
#                 "release_year": movie["release_date"][:4],
#                 "plot": movie["overview"],
#                 "cast": [],  # You can fetch cast details from a separate API endpoint if available
#                 "rating": movie["vote_average"],
#             }
#             return render_template("movie_details.html", movie=movie_details)

#     return jsonify({"error": "Movie not found"}), 404

# # for all movies
# @app.route("/movies", methods=["GET"])
# def get_all_movies():
#     api_key = request.args.get("api_key")
#     response = requests.get(f"{MOVIE_API_BASE_URL}discover/movie", params={"api_key": api_key})
#     data = response.json()
#     if "results" in data:
#         movies_list = []
#         for movie in data["results"]:
#             movies_list.append(movie["title"])
#         return render_template("all_movies.html", movies=movies_list)

#     return jsonify({"error": "No movies found"}), 404




# 2nd version
@app.route("/movies/<string:movie_name>", methods=["GET"])
def get_movie_details(movie_name):
    api_key = request.args.get("api_key")
    response = requests.get(f"{MOVIE_API_BASE_URL}search/movie", params={"api_key": api_key, "query": movie_name})
    data = response.json()
    if "results" in data:
        if len(data["results"]) > 0:
            movie = data["results"][0]
            return render_template("movie_details.html", movie=movie)

    return jsonify({"error": "Movie not found"}), 404

@app.route("/movies", methods=["GET"])
def get_all_movies():
    api_key = request.args.get("api_key")
    response = requests.get(f"{MOVIE_API_BASE_URL}discover/movie", params={"api_key": api_key})
    data = response.json()
    if "results" in data:
        return render_template("all_movies.html", movies=data["results"])

    return jsonify({"error": "No movies found"}), 404




if __name__ == "__main__":
    app.run(debug=True)
