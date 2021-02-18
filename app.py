import os
from flask import Flask, json,abort, jsonify, request
from flask_cors import CORS
from models import Actor, Movie, setup_db

def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)
    #endpoints for actors and movies
    @app.route('/actors', methods=['GET'])
    def show_actors():
        actors = Actor.query.all()
        if actors:
            formatted_actors= [i.format() for i in actors]
            return jsonify({
                "success" : True,
                "actors" : formatted_actors
            })
        else:
            abort(422)
    
    @app.route('/movies', methods=['GET'])
    def show_movies():
        movies = Movie.query.all()
        if movies:
            formatted_movies = [m.format() for m in movies]
            return jsonify({
                "success" : True,
                "movies" : formatted_movies
            })
        else:
            abort(422)

    @app.route('/movies/<movie_id>', methods=['DELETE', 'PATCH'])
    def patch_and_delete_movie(movie_id):
        movie = Movie.query.get(movie_id)
        if  movie is None : 
            abort(404)

        if request.method == "PATCH":
            data = request.get_data()
            data = json.loads(data)
            try:
                movie.title = data['title']
                movie.release_date = data['release_date']
            except:
                abort(400)
            try:
                movie.update()
                return jsonify({
                    "success": True,
                    "updated movie": movie.format()
                })
            except:
                abort(500)

        if request.method == "DELETE":
            try:
                movie.delete()
                return jsonify({
                    "success" : True,
                    "deleted movie": movie.format()
                })
            except:
                abort(500)
    
    @app.route('/actors/<actor_id>', methods = ["PATCH", "DELETE"])
    def patch_and_delete_actor(actor_id):
        actor = Actor.query.get(actor_id)
        if actor is None:
            abort(404)
        if request.method == "PATCH":
            data = request.get_data()
            data = json.loads(data)
            try:
                actor.name = data['name']
                actor.age = data['age']
                actor.gender = data['gender']
            except:
                abort(400)
                
            try:
                actor.update()
                return jsonify({
                    "success" : True,
                    "actor" : actor.format()
                })
            except:
                abort(500)
        if request.method == "DELETE":
            try:
                actor.delete()
                return jsonify({
                    "success": True,
                    "deleted actor": actor.format()
                })
            except:
                abort(500)
        
    @app.route('/movies/new', methods=["POST"])
    def create_movie():
        data = request.get_data()
        data = json.loads(data)
        try:
            title = data['title']
            release_date = data['release_date']
        except:
            abort(400)
        movie = Movie(title= title, release_date=release_date)
        try:
            movie.insert()
            return jsonify({
                "success": True,
                "movie": movie.format()
            })
        except:
            abort(500)
        
    @app.route('/actors/new', methods=["POST"])
    def create_actor():
        data = request.get_data()
        data = json.loads(data)
        try:
            name = data['name']
            age = data['age']
            gender = data['gender']
        except:
            abort(400)

        actor = Actor(name = name, age=age, gender=gender)
        try:
            actor.insert()
            return jsonify({
                "success": True,
                "actor": actor.format()
            })
        except:
            abort(500)

    #error handlers
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'request does not have the specified parameters'
        }), 400

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            'success': False,
            'error': 401,
            'message': 'credentials are not authorized'
        }),401
    
    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({
            'success': False,
            'error': 403,
            'message': 'you dont have permission to access this resource'
        }), 403
    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'the requested resource does not exist'
        }), 404

    @app.errorhandler(422)
    def unproccessable(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'unproccessable'
        }), 422
    
    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            'success': False,
            'error': 500,
            'message': 'unexpected error at the server'
        }), 500
                
    return app
app = create_app()
if __name__ == '__main__':
    app.debug = True
    app.run()