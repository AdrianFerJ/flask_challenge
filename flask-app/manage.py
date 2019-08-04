from flask.cli import FlaskGroup

from project import app, db


cli = FlaskGroup(app)


# Register commands

@cli.command('recreate_db')
def recreate_db():
    """ Func to recreate db. 
        ATTENTION, existing dbs will be deleted
    """
    db.drop_all()
    db.create_all()
    db.session.commit()

if __name__ == '__main__':
    cli()