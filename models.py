from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"

class User(db.Model):
    """ User. """

    __tablename__ = "users"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    first_name = db.Column(db.String(50),
                     nullable=False)
    last_name = db.Column(db.String(50),
                     nullable=False)
    image_url = db.Column(db.String(150),
                     nullable=False,
                     default=DEFAULT_IMAGE_URL)

    def __repr__(self):
        return f'<User {self.id} {self.first_name} {self.last_name}>'

class Post(db.Model):
    """ Post. """

    __tablename__ = "posts"

    id = db.Column(db.Integer, 
        primary_key=True,
        autoincrement=True)
    title = db.Column(db.String(100), 
        nullable=False)
    content = db.Column(db.Text, 
        nullable=False)
    created_at = db.Column(db.DateTime, 
        default=db.func.now())
    user_id = db.Column(db.Integer, 
        db.ForeignKey('users.id'))
    
    user = db.relationship('User', backref = 'posts')

    def __repr__(self):
        return f'<Post {self.title} {self.created_at} by {self.user.first_name} {self.user.last_name}>'


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
