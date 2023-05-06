# Dictionary of movies
# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

# 1. Write a function that takes a single movie and returns True if its IMDB score is above 5.
import movies

def goodmovie (movies, movie_name):
    curr_movie = dict(())
    for movie in movies:
        if movie["name"] == movie_name:
            curr_movie = movie
    return curr_movie["imdb"] > 5.5

print(goodmovie (movies, "Hitman"))

# 2. Write a function that returns a sublist of movies with an IMDB score above 5.5.

def goodmovieslist(movies):
    good_movies = []
    for movie in movies:
        if movie["imdb"] > 5.5:
            good_movies.append(movie["name"])
    return good_movies

print(goodmovieslist(movies))

# 3. Write a function that takes a category name and returns just those movies under that category.

def categoryfilma( movies, category):
    movieslist = []
    for movie in movies:
        if movie['category'] == category:
            movieslist.append(movie)
    return movieslist

print(categoryfilma(movies, "Drama"))
print(categoryfilma(movies, "Suspense"))

# 4. Write a function that takes a list of movies and computes the average IMDB score.

def ortasharatingis(movies):
    sum = 0
    num_movies = len(movies)
    for movie in movies:
        sum += movie["imdb"]
    return sum/num_movies

print(ortasharatingis(movies))

# 5. Write a function that takes a category and computes the average IMDB score.
def categorydinortashasy(movies, category):
    sum = 0
    num_movies = 0
    for movie in movies:
        if movie['category'] == category:
            sum += movie['imdb']
            num_movies += 1
    return sum / num_movies

print(categorydinortashasy(movies, 'Suspense'))
