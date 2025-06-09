from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flasgger import Swagger
from config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    Swagger(app, template_file="swagger/docs.yaml")

    with app.app_context():
        from routes.event_routes import event_bp
        from routes.registration_routes import registration_bp
        app.register_blueprint(event_bp)
        app.register_blueprint(registration_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
