import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    DEBUG = False

    CSRF_ENABLED = True

    SECRET_KEY = 'SECRET_KEY'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
