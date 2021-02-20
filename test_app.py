import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Actor, Movie

#THIS TESTCASE IS MADE TO TEST THE BEHAVIOR OF THE ENDPOINTS BEFORE THE AUTHENTICATION ADDED
#AUTHENTICATION AND ROLE BASED ACCESS TEST IS AT THE POSTMAN COLLECTION

class AgencyTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        setup_db(self.app)
        
        self.new_movie= {
            'title': 'test case movie',
            'release_date': '12-sep-1990'
        }

        self.new_movie_error= {
            'title' : 'error movie'
        }

        self.new_actor= {
            'name': 'test case actor',
            'age': 40,
            'gender': 'male'
        }

        self.new_actor_error= {
            'name': 'error actor'
        }

        with self.app.app_context():
            self.db =SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()
    
    def tearDown(self):
        pass

    def test_get_movies(self):
        res = self.client().get('/movies')
        data = res.get_json()
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    def test_get_actors(self):
        res = self.client().get('/actors')
        data = res.get_json()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])
    
    def test_post_movie(self):
        res = self.client().post('/movies/new', json=self.new_movie)
        data = res.get_json()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    def test_post_movie_error(self):
        res = self.client().post('/movies/new', json=self.new_movie_error)
        data = res.get_json()
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])
    
    def test_post_actor(self):
        res = self.client().post('/actors/new', json = self.new_actor)
        data = res.get_json()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    def test_post_actor_error(self):
        res = self.client().post('/actors/new', json = self.new_actor_error)
        data = res.get_json()
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])
    
    def test_patch_movie(self):
        res = self.client().patch('/movies/4', json = self.new_movie)
        data = res.get_json()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['updated movie'])
    
    def test_patch_movie_NotFound(self):
        res = self.client().patch('/movies/1000', json = self.new_movie)
        data = res.get_json()
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])

    def test_patch_movie_BadReq(self):
        res = self.client().patch('/movies/4', json = self.new_movie_error)
        data = res.get_json()
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])

    def test_patch_actor(self):
        res = self.client().patch('/actors/4', json = self.new_actor)
        data = res.get_json()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['updated actor'])
    
    def test_patch_actor_NotFound(self):
        res = self.client().patch('/actors/1000', json = self.new_actor)
        data = res.get_json()
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])

    def test_patch_actor_BadReq(self):
        res = self.client().patch('/actors/4', json = self.new_actor_error)
        data = res.get_json()
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])

    def test_delete_movie(self):
        res = self.client().delete('/movies/5')
        data = res.get_json()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted movies'])
    
    def test_delete_movie_NotFound(self):
        res = self.client().delete('movies/1000')
        data = res.get_json()
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])

    def test_delete_actor(self):
        res = self.client().delete('/actors/4')
        data = res.get_json()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted actor'])

    def test_delete_actor_NotFound(self):
        res = self.client().delete('/actors/1000')
        data = res.get_json()
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])
        

    

if __name__ == '__main__':
    unittest.main()