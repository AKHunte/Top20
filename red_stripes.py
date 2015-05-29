#!/usr/bin/env python2.6

from operator import itemgetter
import sys
import ast
import operator

cat = {} #<k,v> = <movie pair, count >

current_stripe= {}
movie = None
dic_counts = {}

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace

    #print line
    # parse the input we got from mapper.py
    movie, stripe = line.split('\t', 1)
     
    stripe = ast.literal_eval(stripe)
 
    #convert stripe into a dict
    stripe = dict(stripe)
   
    #print stripe	    
 #   print movie, stripe	    
	
    #Add the first movie

    #loop over the keys of the stripe
    #and make pairs
    for k in stripe:
	if int(movie) < int(k):
	        newpair  = str(movie) + ' ' + str(k)
	else:
		newpair = str(k) + ' ' + str(movie)
        #count the occurancies of the movies 
	if newpair in cat:
		cat[newpair] += stripe[k]
	else:
		cat[newpair] = stripe[k]



#Print 
for k in cat:
	m1, m2 = k.split()
	print m1, m2, cat[k]

