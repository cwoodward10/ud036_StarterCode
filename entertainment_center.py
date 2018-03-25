#note: used python 3.5 to write this, idk if its that different from 2.7

#import these modules
import fresh_tomatoes
import media
import csv

#fresh_tomatoes requires a list of movies
movies_list = []


#Chose to use a CSV file to store the information about the movies.
#This way, I do not muddle up this code with too many class creations
#but instead just appended each row of the csv file to the movies_list.

with open('Movies_CSV.csv') as  csvfile:
    reader = csv.DictReader(csvfile)

    for movie in reader:
        title = str(movie['Movie Title'])
        poster = str(movie['Movie Poster URL'])
        trailer = str(movie['Movie Trailer URL'])
        movie_id = str(movie['Movie ID']) #name as appears in movies_list

        movies_list.append(media.Movie(title, poster, trailer, movie_id))

#run to create the HTML file for the movies webpage
fresh_tomatoes.open_movies_page(movies_list)
