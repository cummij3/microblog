import os

class Config(object):
	SECRET_KEY = os.environ.get('SECTER_KEY') or 'you-will-never-guess'