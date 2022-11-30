"""Seed file to make sample data for users db."""

from models import User, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add pets
bob = User(first_name='Bob', last_name="Marley", image_url="https://images.theconversation.com/files/144359/original/image-20161103-25349-1jdv0b3.jpg")
homer = User(first_name='Homer', last_name="Simpson", image_url="https://i1.sndcdn.com/avatars-000661668236-u0xkoy-t500x500.jpg")
walter = User(first_name='Walter', last_name="Sobchak", image_url="https://pbs.twimg.com/profile_images/986624504616144896/kP8AURXj_400x400.jpg")

# Add new objects to session, so they'll persist
db.session.add(bob)
db.session.add(homer)
db.session.add(walter)

# Commit--otherwise, this never gets saved!
db.session.commit()