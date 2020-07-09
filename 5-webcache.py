import urllib.request
import datetime

"""
- create a web client, that on the first iteration of fetching a url it then caches the url and response in a hash table
- on subsequent calls the web response is pulled from the cache
- URL -> KEY
- PAGE DATA -> VALUE

"""
# first pass

# let's make a class to hold a cache entry

# store the url
# store the data

# let's plan out how we will approach this

# take input from user set it to url

# some data store

# check if the key is in the cache
    # if it is then set the cache at the url to an entry

    #set our data to the entry / the data that was returned
    # print getting from cache

# if our data is still none
    # then get the data from the server
    # call to urlopen passing in the url
    # save the response
    # take the response data and put it in the data variable
    # print getting from server

    # store the data in the cache

    # close connection




# second pass

# let's make a class to hold a cache entry

# store the url
# store the data
# store a timestamp

# some expiry time

# let's plan out how we will approach this
# keep looping
    # take input from user set it to url

    # some data store

    # check if the key is in the cache
        # if it is then set the cache at the url to an entry
        # has our cache timeout expired
        
        # if it has not expired
            # set our data to the entry / the data that was returned
            # print getting from cache

    # if our data is still none
        # then get the data from the server
        # call to urlopen passing in the url
        # save the response
        # take the response data and put it in the data variable
        # print getting from server

        # store the data in the cache
        # create a cache entry object and store that in the cache

        # close connection

