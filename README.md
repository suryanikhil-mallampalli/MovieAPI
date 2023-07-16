# TDP-Vista-MovieAPI
Objective:
This solution aims to create a Flask API that includes authentication using
an API key. The API allows users to retrieve movie details by sending a movie name
to the API endpoint and also provides a list of all available movies in the form of JSON. To accomplish this, I have utilized a free open-source movie data source.

Features of API:
1. This Flask API with the following endpoints:
- GET /movies/movie_name: Retrieves movie details based on the provided movie_name.
- GET /movies`: Retrieves a list of all available movies that were recently released.
2. Implemented authentication using an API key. The API key should be passed as a
header in the request in order to get a response.
- The API key is stored securely and has not been hardcoded in the application code.
- If the API key is missing or invalid, the API returns a 401 Unauthorized status
code.
3. I have used Utilized the movie data source to fetch movie details and the movie list from the below source
- The Movie Database API (https://www.themoviedb.org/documentation/api)

4. This API Returns the movie details and movie list in the response:
- The `GET /movies/` endpoint  returns the relevant details of the movie, such
as title, release year, popularity, and rating.
- The `GET /movies` endpoint returns a list of all available movies.
- The responses were in JSON format.
5. - The authentication is enforced for both endpoints (`/movies` and `/movies/`).
- If the API key is missing or invalid, the API returns a 401 Unauthorized status
code.
