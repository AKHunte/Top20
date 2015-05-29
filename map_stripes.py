#!/usr/bin/env python2.6

#Author: Aisha Hunte
#Date: March 22, 2015

import sys
import os
#import collections
from collections import defaultdict

favorites = defaultdict(list) #dict <k,v> = <userid, [list of favorite movies]>
pairs = {} #<k,v> <pair, count of pair>
dict_stripe = defaultdict(dict)

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
	
    # split the line into words
    #user, movie, rating, time = line.split('\t')
    user, movie, rating, time = line.split('::')
    user = int(user)
    movie = int(movie)    
    rating = int(rating)

    #skip movies with ratings less than 4 
    if rating < 4:
        #skip ratings less than 4
    	continue    
    #Build dictionary
    if user in favorites.keys():
    	if movie in favorites[user]:
		continue
	else:
        	favorites[user].append(movie) 
    else:
    	favorites[user].append(movie)

for user in favorites.keys():
    #only considered users that have rated atleast two movies
    if len(favorites[user]) > 1:
        movies = list(favorites[user])
	movies = map(int, movies)
        #Sort the list
        sorted_movies = sorted(movies)
        #loop through and count all pairs
	for i in xrange(0,len(sorted_movies)):
		for j in xrange (i+1,len(sorted_movies)): 
                     #make pair m1 m2 where m1 < m2
		     if int(sorted_movies[i]) < int(sorted_movies[j]):
		     	pair = str(sorted_movies[i]).strip(), str(sorted_movies[j]).strip() 
		     else:
		     	pair = str(sorted_movies[j]).strip(), str(sorted_movies[i]).strip() 
		     #count pairs
                     if pair in pairs:
			pairs[pair]+=1
		     else:
                        pairs[pair]= 1

# Make stripes
for pair  in pairs:
	m1, m2 = pair[0], pair[1]
	dict_stripe[m1][m2]= pairs[pair]

#Emit stripes
for k in dict_stripe:
	print str(k), '\t', str(dict_stripe[k])
