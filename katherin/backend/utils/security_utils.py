"""
General suppotive functions related to ensuring application security
"""
import string, random


def generate_token(size=64, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
	"""Generates a random string token"""
	return ''.join(random.choice(chars) for x in range(size))
	