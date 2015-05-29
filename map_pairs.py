#!/usr/bin/env python2.6

#Author: Aisha Hunte
#Date: March 22, 2015 

import sys
import os
from collections import defaultdict

favorites = defaultdict(list) #dict <k,v> = <userid, [list of favorite movies]>
total =0 # total count of movies given a rating of 4 or higher  


# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
	
    # split the line into words
    #user, movie, rating, time = line.split('\t')
    user, movie, rating, time = line.split('::')
    user = user.strip()
    movie = movie.strip()
    rating = rating.strip()
    user = int(user)
    movie = int(movie)    
    rating = int(rating)
   
    #skip movies with ratings less than 4 
    if rating < 4:
    	continue    
    #Build dictionary
    if user in favorites.keys():
	if movie in favorites[user]:
		continue
	else:
        	favorites[user].append(movie) 
    else:
    	favorites[user].append(movie)


#Emit each pair of movies with count of 1, <k,v> = <m1 m2, 1>
for user in favorites.keys():
    if len(favorites[user]) > 1:
        movies = list(favorites[user])
	movies = map(int, movies)
        #Sort the list
        sorted_movies = sorted(movies)
        #loop through the list and make pairs
	for i in xrange(0,len(sorted_movies)):
		for j in xrange (i+1,len(sorted_movies)): 
	            # m1 should be less than m2
		    #Emit Pairs
		    print str(sorted_movies[i]).strip(),str(sorted_movies[j]).strip(),'\t', '1'

