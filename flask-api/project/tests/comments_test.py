import json
import unittest
from api import app, api, COMMENTS

class CommentsTestCase(unittest.TestCase):
    """All tests for the API"""

    def test_get_comments_list(self):
        """Check that GET method returns all objects from DB"""
        tester = app.test_client(self)
        rv = tester.get('/', content_type='html/text')
        self.assertEqual(rv.status_code, 200)
        num_comments = len(COMMENTS)
        data = json.loads(rv.data)
        self.assertEqual(num_comments, len(data))

    def test_post_new_comment(self):
        """Check that a new entry is created making a proper POST"""
        # payload = json.dumps({
        payload = {
            'title': 'Testitle',
            'text' : 'Text body'
        }
        tester = app.test_client(self)
        rv = tester.post('/', data=payload, follow_redirects=True)
        self.assertEqual(rv.status_code, 201)
        data = json.loads(rv.data.decode())
        self.assertEqual('success', data['status'])
        self.assertEqual(payload, data['data'])

    # def test_handle_incorrect_post(self):
    #     """Check proper handling of incorrect POSTs"""
    #     self.assertTrue(tester)

if __name__ == '__main__':
    unittest.main()