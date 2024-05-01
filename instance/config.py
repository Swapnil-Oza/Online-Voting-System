import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///{}'.format(os.path.join(os.path.dirname(__file__), 'app.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
