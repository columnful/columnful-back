import requests
import json
from pprint import pprint
import pdb

from tmdb_helper import TMDBHelper



def get_movie_popular():
    movies_db = []
    actors_list_db = []
    tmdb_helper = TMDBHelper('TMDB_API_KEY')

    for i in range(1, 500):
        request_url = tmdb_helper.get_request_url(method = '/movie/popular', language = 'ko', page=i)
        response = requests.get(request_url).json()
        movies = response['results']

        for data in movies:
            movie_id = data.get('id')

            credits_request_url = tmdb_helper.get_request_url(method =f'/movie/{movie_id}/credits', language = 'ko')
            credits_info = requests.get(credits_request_url).json()
            # pdb.set_trace()

            actors = credits_info.get('cast')
            directors = credits_info.get('crew')
            actors_list = []
            directors_list = []

            for actor in actors:
                if actor['order'] < 10:
                    actors_list.append(actor['id'])
                    if actor not in actors_list_db:
                        actors_list_db.append(actor['id'])

            for director in directors:
                if director['job'] == 'Director':
                    directors_list.append(director['id'])
            data['actors'] = actors_list
            data['directors'] = directors_list
            # pdb.set_trace()
            results = {
                'model': 'movies.movie',
                'fields': data
            }

            movies_db.append(results)

        return movies_db, actors_list_db



def get_actors(actors_id_list):
    tmdb_helper = TMDBHelper('TMDB_API_KEY')
    actors_db = []

    for actor_id in actors_id_list:
        actor_request_url = tmdb_helper.get_request_url(method=f'/person/{actor_id}', language = 'ko')
        actor = requests.get(actor_request_url).json()

        results = {
            'model': 'movies.actor',
            'fields': {
                'id': actor['id'],
                'name': actor['name'],
                'also_known_as': actor['also_known_as'],
                'gender': actor['gender'],
                'profile_path': actor['profile_path']
            }
        }

        actors_db.append(results)
    
    return actors_db



def to_json(filename, data):
    with open(filename, 'w', encoding='UTF-8') as filename:
        json.dump(data, filename, ensure_ascii=False, indent='\t')



if __name__ == '__main__':

    movies, actors_list = get_movie_popular()
    actors = get_actors(actors_list)

    to_json('../fixtures/movies.json', movies)
    to_json('../fixtures/actors.json', actors)

    # to_json('movies.json', movies)
    # to_json('actors.json', actors)

    
