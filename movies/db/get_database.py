import requests
import json
from pprint import pprint
import pdb

from tmdb_helper import TMDBHelper



def get_movies_popular():
    movies_db = []
    actors_list_db = []
    directors_list_db = []
    tmdb_helper = TMDBHelper('d96fad9400bff08e7653e874066ac99b')

    for i in range(1, 500):
        request_url = tmdb_helper.get_request_url(method = '/movie/popular', language = 'ko', page=i)
        response = requests.get(request_url).json()
        movies = response['results']

        for data in movies:
            movie_id = data.get('id')

            credits_request_url = tmdb_helper.get_request_url(method =f'/movie/{movie_id}/credits', language = 'ko')
            credits_info = requests.get(credits_request_url).json()
            # pdb.set_trace()

            keywords_request_url = tmdb_helper.get_request_url(method =f'/movie/{movie_id}/keywords', language = 'ko')
            keywords_data = requests.get(keywords_request_url).json()

            actors = credits_info.get('cast')
            directors = credits_info.get('crew')
            keywords = keywords_data.get('keywords')

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
                    if director not in directors_list_db:
                        directors_list_db.append(director['id'])

            data['actors'] = actors_list
            data['directors'] = directors_list
            data['keywords'] = keywords

            # pdb.set_trace()
            results = {
                'model': 'movies.movie',
                'fields': data
            }

            movies_db.append(results)

        return movies_db, actors_list_db, directors_list_db



def get_people(person_ids, job_string):
    tmdb_helper = TMDBHelper('d96fad9400bff08e7653e874066ac99b')
    people_db = []

    for person_id in person_ids:
        person_request_url = tmdb_helper.get_request_url(method=f'/person/{person_id}', language = 'ko')
        person = requests.get(person_request_url).json()

        results = {
            'model': f'movies.{job_string}',
            'fields': {
                'id': person['id'],
                'name': person['name'],
                'also_known_as': person['also_known_as'],
                'gender': person['gender'],
                'profile_path': person['profile_path']
            }
        }

        people_db.append(results)
    
    return people_db



def to_json(filename, data):
    with open(filename, 'w', encoding='UTF-8') as filename:
        json.dump(data, filename, ensure_ascii=False, indent='\t')



if __name__ == '__main__':

    movies, actors_list, directors_list = get_movies_popular()

    actors = get_people(actors_list, 'actor')
    directors = get_people(directors_list, 'director')

    to_json('../fixtures/movies.json', movies)
    to_json('../fixtures/actors.json', actors)
    to_json('../fixtures/directors.json', directors)
