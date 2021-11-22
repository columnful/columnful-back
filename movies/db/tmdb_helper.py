import requests
import json
from pprint import pprint

class TMDBHelper:

    def __init__(self, api_key=None):
        self.api_key = api_key


    def get_request_url(self, method='/movie/popular', **kwargs):
        base_url = 'https://api.themoviedb.org/3'
        request_url = base_url + method
        request_url += f'?api_key={self.api_key}'

        for k, v in kwargs.items():
            request_url += f'&{k}={v}'

        return request_url
    