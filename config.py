class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@localhost/eventdb"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER = {
        'title': 'Event Management API',
        'uiversion': 3
    }
