"""
Custom exceptions. Used in code as an indicator that Exception contains sane message
"""


class CreateInstanceException(Exception):
	"""Raised whenever model instance is failed to create"""