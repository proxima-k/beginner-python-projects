# https://github.com/jorgegonzalez/beginner-projects#movie-of-the-day
# Finished on 27 Apr 2020
import omdb, random
import json
from json.decoder import JSONDecodeError
import os.path

omdb.set_default('apikey', 'xxx')
new_dict = {'movie_id' : []}

def get_movie():
    while True:
        n = random.randrange(1, 9000001)
        prefix = 'tt'
        movie_id = prefix + str(n).zfill(7)
        movie = omdb.imdbid(movie_id, media_type='movie')
        if len(movie) == 0:
            pass
        else:
            if movie['type'] != 'movie':
                pass
            else:
                break

    return movie

def display_movie(movie):
    print('Title: ' + movie['title'])
    print('Year: ' + movie['year'])
    print('Movie length: ' + movie['runtime'])
    print('Genre: ' + movie['genre'])
    print('IMDB ID: ' + movie['imdb_id'])

if os.path.exists('movie_id.txt'):
    with open('movie_id.txt', 'r') as rf:
        data = json.load(rf)
        existing_id = data['movie_id']
        while True:
            movie_dict = get_movie()
            if movie_dict['imdb_id'] not in existing_id:
                break
            else:
                print("Coincidence!\n")
                pass
        movie_id = movie_dict['imdb_id']
        display_movie(movie_dict)
        data['movie_id'].append(movie_id)
        with open('movie_id.txt', 'w+') as wf:
            json.dump(data, wf)
else:
    with open('movie_id.txt', 'w+') as nf:
        movie_dict = get_movie()
        movie_id = movie_dict['imdb_id']
        display_movie(movie_dict)
        new_dict['movie_id'].append(movie_id)

        json.dump(new_dict, nf)
