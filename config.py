import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'vet34td21123W@BNJTHF'