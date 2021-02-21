

## Casting agency api

This is a casting agency api which having actors and movies.

## Motivation
This project is my final project at the FSND from udacity, i came a long way and i am was really excited doing this project because it was intersting and challenging, and also to finally have my degree.
applying everything i learned during the course was a really fun and important experience.


## Getting Started
you will need to use postman or curl to access this api and it's endpoints

## Dependcies and for developers
you will need flask and sqlalchemy packages to run this project, all required packages are in requirements.txt
the api entry point is app.py where all the endpoints are there.
models.py is associated with tables and objects and their functions.
auth.py is for auth0 authentication and creating the "@requires_auth" decorator.

##### Base url

- https://casting-agency-capstoneproj.herokuapp.com


## API Reference
the "/" endpoint can be publicly accessed to check the health of the api.

-All of the endpints requires authentication and they will be passed as a Bearer Token along the request so endpoints can be accessed, This applies on ALL the coming endpoints.
-All requests that containing a body must be JSON formatted.

url : '/movies', method-allowed : GET, body: None
    this url will return to you all the available movies in the database,status code 200
    and the response body will be like this {
    'success':true,
    movies : example name,
    }
    
url : '/actors', method-allowed : GET, body: None
    this url will return to you all the available actors in the database,status code 200
    and the response body will be like this {
    'success':true,
    actors : example name,
    }
    

url : '/movies/new' method-allowed: POST , body:{"title": string, "release_date": string}
    this will allow you to post a movie in the database using the body and variable names as shown.
    in a successfull transaction the reply should be with status code 200 and looking like this:
    {
        'success': True,
        'movie': example
    }
    
url : '/actors/new' method-allowed: POST , body:{"name": string, "gender": string, "age": int}
    this will allow you to post an actor in the database using the body and variable names as shown.
    in a successfull transaction the reply should be with status code 200 and looking like this:
    {
        'success': True,
        'actor': example
    }

url : '/movies/movie_id' method-allowed: PATCH , body:{"title": string, "release_date": string}
    this will allow you to patch a movie in the database using the body and passing it's id in the url and variable names as shown.
    in a successfull transaction the reply should be with status code 200 and looking like this:
    {
        'success': True,
        'updated movie': example
    }
    
url : '/actors/actor_id' method-allowed: PATCH , body:{"name": string, "gender": string, "age": int}
    this will allow you to patch an actor in the database using the body and variable names and passing it's id in the url as shown.
    in a successfull transaction the reply should be with status code 200 and looking like this:
    {
        'success': True,
        'updated actor': example
    }
    
url : '/movies/movie_id' method-allowed: DELETE , body:None
    this will allow you to delete a movie in the database by passing it's id in the url.
    in a successfull transaction the reply should be with status code 200 and looking like this:
    {
        'success': True,
        'deleted movie': example
    }

url : '/actors/actor_id' method-allowed: DELETE , body:None
    this will allow you to delete aan actor in the database by passing it's id in the url.
    in a successfull transaction the reply should be with status code 200 and looking like this:
    {
        'success': True,
        'deleted actor': example
    }

and this is all endpoint for the api.

And for the roles at this api:
    Casting assistant : can only view actors and movies.
    permissions:
        get:actors
        get:movies
    executive manager: can add, view, modify, delete actors and movies.
    permissions:
        get:actors
        get:movies
        post:actors
        post:movies
        patch:actors
        patch:movies
        delete:actors
        delete:movies


# Deployment N/a
heroku.

# Authors
    moatasem abdelkader
    
# Acknowledgements 
the amazing teachers and reviewrs of Udacity