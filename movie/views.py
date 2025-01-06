from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .utils import fetch

@require_http_methods(["GET"])
def popular_movies(request):
    page = request.GET.get('page', 1)
    try:
        data = fetch("movie/popular", {"language": "en-US", "page": page})
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({"error": f"An unexpected error occurred: {str(e)}"}, status=500)

@require_http_methods(["GET"])
def top_rated_movies(request):
    page = request.GET.get('page', 1)
    try:
        data = fetch("movie/top_rated", {"language": "en-US", "page": page})
        sorted_rating = sorted(data.get("results", []), key=lambda x: x.get("vote_average", 0), reverse=True)
        return JsonResponse({"top_movies": sorted_rating[:10]})
    except Exception as e:
        return JsonResponse({"error": f"An unexpected error occurred: {str(e)}"}, status=500)

@require_http_methods(["GET"])
def search_movies(request):
    query = request.GET.get("query", '')
    if not query:
        return JsonResponse({"error": "Query parameter is required"}, status=400)
    try:
        data = fetch("search/movie", {"query": query, "language": "en-US"})
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({"error": f"An unexpected error occurred: {str(e)}"}, status=500)

@require_http_methods(["GET"])
def now_playing(request):
    page = request.GET.get('page', 1)
    try:
        data = fetch("movie/now_playing", {"language": "en-US", "page": page})
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({"error": f"An unexpected error occurred: {str(e)}"}, status=500)

@require_http_methods(["GET"])
def upcoming(request):
    page = request.GET.get('page', 1)
    try:
        data = fetch("movie/upcoming", {"language": "en-US", "page": page})
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({"error": f"An unexpected error occurred: {str(e)}"}, status=500)
@require_http_methods(["GET"])
def filter(request):
    genre=request.GET.get('genre',None)
    release_year=request.GET.get('release_year',None)
    genres = {
    "Action": 28,
    "Adventure": 12,
    "Animation": 16,
    "Comedy": 35,
    "Crime": 80,
    "Documentary": 99,
    "Drama": 18,
    "Family": 10751,
    "Fantasy": 14,
    "History": 36,
    "Horror": 27,
    "Music": 10402,
    "Mystery": 9648,
    "Romance": 10749,
    "Science Fiction": 878,
    "TV Movie": 10770,
    "Thriller": 53,
    "War": 10752,
    "Western": 37
    }
    genre_id=genres.get(genre)
    params = {
    "language": "en-US",
    "with_genres": genre_id if genre_id else None,
    "primary_release_year": release_year,
    "page": request.GET.get("page", 1),  
    }
    params = {k: v for k, v in params.items() if v is not None}
    try:
        data = fetch("discover/movie", params)
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({"error": f"An unexpected error occurred: {str(e)}"}, status=500)

@require_http_methods(["GET"])
def compare(request):
    movie1_title = request.GET.get('movie1', None)
    movie2_title = request.GET.get('movie2', None)

    if not movie1_title or not movie2_title:
        return JsonResponse({"error": "Both movie1 and movie2 parameters are required."}, status=400)

    try:
        movie1_data = fetch("search/movie", {"query": movie1_title, "language": "en-US"})
        movie2_data = fetch("search/movie", {"query": movie2_title, "language": "en-US"})

        if "results" not in movie1_data or "results" not in movie2_data:
            return JsonResponse({"error": "Error fetching movie data."}, status=500)

        movie1_id = movie1_data["results"][0]["id"]
        movie2_id = movie2_data["results"][0]["id"]

        data1 = fetch(f"movie/{movie1_id}", {"language": "en-US"})
        data2 = fetch(f"movie/{movie2_id}", {"language": "en-US"})

        movie1_details = {
            "title": data1.get("title"),
            "release_date": data1.get("release_date"),
            "vote_average": data1.get("vote_average"),
            "genres": [genre['name'] for genre in data1.get("genres", [])]
        }

        movie2_details = {
            "title": data2.get("title"),
            "release_date": data2.get("release_date"),
            "vote_average": data2.get("vote_average"),
            "genres": [genre['name'] for genre in data2.get("genres", [])]
        }

        comparison = {
            "movie1": movie1_details,
            "movie2": movie2_details,
            "higher_vote_average": movie1_details["title"] if movie1_details["vote_average"] > movie2_details["vote_average"] else movie2_details["title"]
        }

        return JsonResponse(comparison)

    except Exception as e:
        return JsonResponse({"error": f"An unexpected error occurred: {str(e)}"}, status=500)

    