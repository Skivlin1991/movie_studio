from db.run_sql import run_sql
from models.movie import Movie


def save(movie):
    sql = "INSERT INTO movies (title, rating) VALUES ( %s, %s )  RETURNING *"
    values = [movie.title, movie.rating]
    results = run_sql(sql, values)
    id = results[0]['id']           
    movie.id = id                    
    return movie  
    
def select_all():
    movies = []  # In case we get `None` back from run_sql

    sql = "SELECT * FROM movies"
    results = run_sql(sql)

    for row in results:
        movie = Movie(row['title'], row['rating'], row['id'] )
        movies.append(movie)
    return movies
    # movie_repository.save(movie_1) 