from app import app

import unittest

class BasicTestCase(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		pass 

	@classmethod
	def tearDownClass(cls):
		pass 

	def setUp(self):
		# creates a test client
		self.app = app.test_client()
		# propagate the exceptions to the test client
		self.app.testing = True 

	def tearDown(self):
		pass 

	def test_home_status_code(self):
		response = self.app.get('/', content_type='html/text')
		# assert the status code of the response
		self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
