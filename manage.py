#!/usr/bin/env python3.5

import os
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from app import create_app
from app.database import db


app = create_app()

app.config.from_object(os.environ['APP_SETTINGS'])


def _make_context():
    return dict(db=db)


manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)
manager.add_command('shell', Shell(make_context=_make_context))


if __name__ == '__main__':
    manager.run()
