"""Seed file to make sample data for users db."""

from models import User, Post, Tag, PostTag, db
from app import app

# Create all tables
db.reflect()
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add users
bob = User(first_name='Bob', last_name="Marley", image_url="https://images.theconversation.com/files/144359/original/image-20161103-25349-1jdv0b3.jpg")
homer = User(first_name='Homer', last_name="Simpson", image_url="https://i1.sndcdn.com/avatars-000661668236-u0xkoy-t500x500.jpg")
walter = User(first_name='Walter', last_name="Sobchak", image_url="https://pbs.twimg.com/profile_images/986624504616144896/kP8AURXj_400x400.jpg")

# Add new objects to session, so they'll persist
db.session.add(bob)
db.session.add(homer)
db.session.add(walter)

# Commit--otherwise, this never gets saved!
db.session.commit()

# Add posts
b1 = Post(title='Greatness', content='The greatness of a man is not in how much wealth he acquires, but in his integrity and his ability to affect those around him positively.', user_id=1)
b2 = Post(title='Happiness', content='Just because you are happy it does not mean that the day is perfect but that you have looked beyond its imperfections.', user_id=1)
h1 = Post(title='Kids are great', content='You can teach them to hate what you hate and, with the Internet and all, they practically raise themselves.', user_id=2)
h2 = Post(title='Overdue book?', content='This is the biggest frame-up since OJ! Wait a minute. Blood in the Bronco. The cuts on his hands. Those Jay Leno monologues. Oh my god, he did it!', user_id=2)
h3 = Post(title='Not Fair', content='Ohh, I have 3 kids and no money. I wish I had no kids and 3 money.', user_id=2)
w1 = Post(title='Nihilists are even worse than Nazis', content='Say what you want about the tenets of National Socialism, Dude, at least it''s an ethos.', user_id=3)
w2 = Post(title='You want a toe? I can get you a toe', content='Hell, I can get you a toe by three o''clock this afternoon, with nail polish.', user_id=3)
w3 = Post(title='A Eulogy For Donny', content='Donny was a good bowler, and a good man. He was one of us. He was a man who loved the outdoors...and bowling. And as a surfer, he explored the beaches of Southern California, from La Jolla to Leo Carrillo and...up to...Pismo. He died, like so many young men of his generation. He died before his time. In your wisdom, Lord, you took him, as you took so many bright, flowering, young men at Khe Sanh, at Langdok, at Hill 364.', user_id=3)

db.session.add(b1)
db.session.add(b2)
db.session.add(h1)
db.session.add(h2)
db.session.add(h3)
db.session.add(w1)
db.session.add(w2)
db.session.add(w3)

db.session.commit()

#Add tags
t1 = Tag(name='Thoughtful')
t2 = Tag(name='Silly')
t3 = Tag(name='Questionable')
t4 = Tag(name='Sincere')

db.session.add(t1)
db.session.add(t2)
db.session.add(t3)
db.session.add(t4)

db.session.commit()

#Add posts_tags
pt1 = PostTag(post_id = '1', tag_id='1')
pt2 = PostTag(post_id = '1', tag_id='4')
pt3 = PostTag(post_id = '2', tag_id='1')
pt4 = PostTag(post_id = '2', tag_id='4')
pt5 = PostTag(post_id = '3', tag_id='2')
pt6 = PostTag(post_id = '3', tag_id='3')
pt7 = PostTag(post_id = '4', tag_id='2')
pt8 = PostTag(post_id = '5', tag_id='2')
pt9 = PostTag(post_id = '6', tag_id='1')
pt10 = PostTag(post_id = '6', tag_id='3')
pt11 = PostTag(post_id = '7', tag_id='2')
pt12 = PostTag(post_id = '7', tag_id='3')
pt13 = PostTag(post_id = '8', tag_id='4')

db.session.add(pt1)
db.session.add(pt2)
db.session.add(pt3)
db.session.add(pt4)
db.session.add(pt5)
db.session.add(pt6)
db.session.add(pt7)
db.session.add(pt8)
db.session.add(pt9)
db.session.add(pt10)
db.session.add(pt11)
db.session.add(pt12)
db.session.add(pt13)

db.session.commit()