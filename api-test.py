import json
import unittest
from api import app, api, COMMENTS

class CommentsTestCase(unittest.TestCase):

    def test_get_comments_list(self):
        """Check that GET method returns all objects from DB"""
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        num_comments = len(COMMENTS)
        data = json.loads(response.data)
        self.assertEqual(num_comments, len(data))


if __name__ == '__main__':
    unittest.main()