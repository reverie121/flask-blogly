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

    tags = db.relationship('Tag', secondary = 'posts_tags', backref='posts')

    def __repr__(self):
        return f'<Post {self.title} {self.created_at} by {self.user.first_name} {self.user.last_name}>'

class Tag(db.Model):
    """ Tag. """

    __tablename__ = "tags"

    id = db.Column(db.Integer, 
        primary_key=True,
        autoincrement=True)
    name = db.Column(db.String(100), 
        nullable=False,
        unique=True)
    
    def __repr__(self):
        return f'<Tag {self.id} {self.name}>'


class PostTag(db.Model):
    """ """

    __tablename__ = "posts_tags"

    post_id = db.Column(db.Integer, 
        db.ForeignKey('posts.id'),
        primary_key=True)
    tag_id = db.Column(db.Integer, 
        db.ForeignKey('tags.id'),
        primary_key=True)

    post = db.relationship('Post', backref = 'posttags')

    tag = db.relationship('Tag', backref = 'posttags')

    def __repr__(self):
        return f'<PostTag {self.post_id} {self.tag_id}>'

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
