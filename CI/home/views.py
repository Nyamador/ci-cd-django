from django.shortcuts import render ,HttpResponse
import json



def index(request):
    return HttpResponse(
        json.dumps(        {
        'id': 14957,
        'url': "https://yts.lt/movie/grand-theft-auto-girls-2020",
        'imdb_code': "tt8985240",
        'title': "Grand Theft Auto Girls",
        'title_english': "Grand Theft Auto Girls",
        'title_long': "Grand Theft Auto Girls (2020)",
        'slug': "grand-theft-auto-girls-2020",
        'year': 2020,
        'rating': 5,
        'runtime': 0,
        'genres': [
        "Thriller"
        ],
        'summary': "A widowed mother must help her teenage daughter escape a life of crime after she becomes embroiled in a dangerous scheme to steal luxury cars for her high school teacher.",
        'description_full': "A widowed mother must help her teenage daughter escape a life of crime after she becomes embroiled in a dangerous scheme to steal luxury cars for her high school teacher.",
        'synopsis': "A widowed mother must help her teenage daughter escape a life of crime after she becomes embroiled in a dangerous scheme to steal luxury cars for her high school teacher.",
        'yt_trailer_code': "",
        'language': "English",
        'mpa_rating': "",
        'background_image': "https://yts.lt/assets/images/movies/grand_theft_auto_girls_2020/background.jpg",
        'background_image_original': "https://yts.lt/assets/images/movies/grand_theft_auto_girls_2020/background.jpg",
        'small_cover_image': "https://yts.lt/assets/images/movies/grand_theft_auto_girls_2020/small-cover.jpg",
        'medium_cover_image': "https://yts.lt/assets/images/movies/grand_theft_auto_girls_2020/medium-cover.jpg",
        'large_cover_image': "https://yts.lt/assets/images/movies/grand_theft_auto_girls_2020/large-cover.jpg",
        'state': "ok",
        }
        )
    )