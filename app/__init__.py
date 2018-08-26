import os
from flask import Flask
from .database import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])

    db.init_app(app)

    with app.test_request_context():
        db.create_all()

    if app.debug:
        try:
            from flask_debugtoolbar import DebugToolbarExtension
            toolbar = DebugToolbarExtension(app)
        except:
            pass

    import app.market.controllers as market
    import app.general.controllers as general
    import app.my_filters as myfilters
    
    app.register_blueprint(market.module)
    app.register_blueprint(general.module)
    app.register_blueprint(myfilters.module)

    return app
