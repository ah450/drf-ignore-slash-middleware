from drf_ignore_slash_middleware import SlashIgnoreMiddleware
from unittest.mock import Mock
import unittest

class TestSlashIgnoreMiddleware(unittest.TestCase):

	def setUp(self):
		self.middleware = SlashIgnoreMiddleware(Mock(return_value=None))
		self.request_with_slash = Mock()
		self.request_without_slash = Mock()
		self.expected_path = '/api/test'
		self.request_with_slash.path = '/api/test/'
		self.request_with_slash.path_info = '/api/test/'
		self.request_without_slash.path = '/api/test'
		self.request_without_slash.path_info = '/api/test'

	def test_with_slash(self):
		self.middleware(self.request_with_slash)
		self.assertEqual(self.request_with_slash.path, self.expected_path)
		self.assertEqual(self.request_with_slash.path_info, self.expected_path)

	def test_without_slash(self):
		self.middleware(self.request_without_slash)
		self.assertEqual(self.request_without_slash.path, self.expected_path)
		self.assertEqual(self.request_without_slash.path_info, self.expected_path)
	