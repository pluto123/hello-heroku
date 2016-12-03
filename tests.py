import unittest
import web

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = web.app.test_client()
        
    def test_index(self):
        rv = self.app.get('/')
        assert b'Hello, Steven Wu' in rv.data
        
if __name__ == '__main__':
    unittest.main()
