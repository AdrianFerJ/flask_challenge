# from app import db
from app import db
from models import Comments

# whipe existing db tables
db.drop_all()

# create the database and the db table
db.create_all()

# commit the changes
db.session.commit()