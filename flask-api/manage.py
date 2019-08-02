from flask.cli import FlaskGroup

from project import app


cli = FlaskGroup(app)


# Registers commands to CLI
@cli.command('recreate_db')
def recreate_db():
    """ Convinient command to recreate db 
        CAREFUL, will whipe out existing db
    """
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == '__main__':
    cli()