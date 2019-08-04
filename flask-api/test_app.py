import unittest
import os
import json

from app import app, db
from models import Comments


TEST_DB = 'test.db'


class BasicTestCase(unittest.TestCase):

    def test_index(self):
        """initial test. ensure flask was set up correctly"""
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_commments_db_exists(self):
        """initial test. ensure that the database exists"""
        print('# HERE', os.listdir())
        tester = os.path.exists("comments.db")
        self.assertTrue(tester)
    
    # def test_test_db_exists(self):
    #     """initial test. ensure that the database exists"""
    #     tester = os.path.exists(TEST_DB)
    #     self.assertTrue(tester)


class CommentsTestCase(unittest.TestCase):
    """All tests for the API"""

    def setUp(self):
        """Set up a blank temp database before each test"""
        basedir = os.path.abspath(os.path.dirname(__file__))
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
            os.path.join(basedir, TEST_DB)
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        """Destroy blank temp database after each test"""
        db.drop_all()

    def test_empty_db(self):
        """Check that database is empty"""
        rv = self.app.get('/')
        # TODO test no entries in empty db
    
    def test_get_comments_list(self):
        """Check that GET method returns all objects from DB"""
        tester = app.test_client(self)

        # Create fake entry
        nc = Comments(title='Test title', text='much more text')
        db.session.add(nc)
        db.session.commit()

        rv = tester.get('/', content_type='html/text')
        self.assertEqual(rv.status_code, 200)
        self.assertIn(b'Test title', rv.data)
    
    # TODO test add_new_comments() functionality 
    

if __name__ == '__main__':
    unittest.main()

