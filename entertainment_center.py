#note: used python 3.5 to write this, idk if its that different from 2.7

#import these modules
import fresh_tomatoes
import media
import csv

#create empty list that will eventually contain all the movie_poster_url
movies_list = []

#import information from the CSV file
#chose to use a CSV file to store the information about the movies
#this way, I do not muddle up this code with too many class creations
#documentation here: https://docs.python.org/3.5/library/csv.html
with open('Movies_CSV.csv') as  csvfile:
    reader = csv.DictReader(csvfile)
    #iterate over each movie in the csv file
    for movie in reader:
        title = str(movie['Movie Title'])
        poster = str(movie['Movie Poster URL'])
        trailer = str(movie['Movie Trailer URL'])
        #movie_id is what shows up if printing the movies_list
        movie_id = str(movie['Movie ID'])
        #append the movies_list with 1 class instance per movie in csv
        movies_list.append(media.Movie(title, poster, trailer, movie_id))

#run to create the HTML file for the movies webpage
fresh_tomatoes.open_movies_page(movies_list)
