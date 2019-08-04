from app import db
from models import Comments

# create the database and the db table
db.create_all()

# commit the changes
db.session.commit()