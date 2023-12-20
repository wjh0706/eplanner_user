from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eplanner.db'

    db.init_app(app)

    from .routes.user_routes import user_blueprint
    app.register_blueprint(user_blueprint)

    logging.basicConfig( level=logging.INFO)


    file_handler = logging.FileHandler('mdwarerecordinglog.log')
    file_handler.setLevel(logging.INFO)


    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)


    logger = logging.getLogger(__name__)
    logger.addHandler(file_handler)

    # Custom middleware of recording log
    class LoggingMiddleware:
        def __init__(self, app):
            self.app = app

        def __call__(self, environ, start_response):

            print(start_response)
            logger.info('Handling request: %s %s', environ['REQUEST_METHOD'], environ['PATH_INFO'])

            def custom_start_response(status, headers, exc_info=None):
                
                print(status)
                logger.info('Response returned: %s', status)

                #
                return start_response(status, headers, exc_info)

            # Use flask to deal with rueqests
            return self.app(environ, custom_start_response)

    app.wsgi_app = LoggingMiddleware(app.wsgi_app)

    return app