import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_rq2.script import RQManager

from app import app, db, rq


app.config.from_object(os.getenv('APP_SETTINGS', 'config.DevelopmentConfig'))

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)
manager.add_command('rq', RQManager(rq))


if __name__ == '__main__':
    manager.run()
