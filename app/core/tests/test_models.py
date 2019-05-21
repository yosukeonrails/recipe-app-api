from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
	def test_create_user_with_email_successful(self):
		"""Test Create a new user with an email is successful"""
		email = 'test@yahoo.com'
		password = 'testpass123'
		usser = get_user_model().objects.create_user(
			email=email,
			password= password
		)

		self.assertEqual(user.email, email)
		self.assertTrue(user.check_password(password))
		