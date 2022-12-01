from unittest import TestCase
from app import app
from models import db, User, Post

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
app.config['SQLALCHEMY_ECHO'] = False

app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()

class UserRoutesTestCase(TestCase):
    """ Tests for Blogly user routes. """

    def setUp(self):
        """Add sample user."""
        User.query.delete()
        Post.query.delete()
        walter = User(first_name='Walter', last_name="Sobchak", image_url="https://pbs.twimg.com/profile_images/986624504616144896/kP8AURXj_400x400.jpg")
        db.session.add(walter)
        db.session.commit()

    def tearDown(self):
        """Clean up any fouled transaction."""
        db.session.rollback()
        
    def test_root(self):
        with app.test_client() as client:
            resp = client.get('/')
            self.assertEqual(resp.status_code, 302)

    def test_users_list(self):
        with app.test_client() as client:
            resp = client.get('/users')
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1 class="h1">Users</h1>', html)
    
    def test_users_new(self):
         with app.test_client() as client:
            resp = client.get('/users/new')
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1 class="h1">Create a user</h1>', html)
        
    # def test_user_submit(self):
    #     with app.test_client() as client:
    #         resp = client.post('/users/new', data = { 'first_name': 'Bob', 'last_name': 'Marley', 'image_url': 'https://images.theconversation.com/files/144359/original/image-20161103-25349-1jdv0b3.jpg'}, follow_redirects=True)
    #         html = resp.get_data(as_text=True)
    #         self.assertEqual(resp.status_code, 200)
    #         self.assertIn('<h1 class="h1">Bob Marley</h1>', html)

    def test_user_details(self):
        with app.test_client() as client:
            resp = client.get('/users/1')
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1 class="h1 mt-2">Walter Sobchak</h1>', html)

    def test_user_delete(self):
        with app.test_client() as client:
            resp = client.post('/users/1/delete', follow_redirects=True)
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1 class="h1">Users</h1>', html)
            self.assertNotIn('<li>', html)
            self.assertNotIn('Walter Sobchak', html)


class PostRoutesTestCase(TestCase):
    """ Tests for Blogly post routes. """

    def setUp(self):
        """Add sample user with posts."""
        User.query.delete()
        Post.query.delete()

        bob = User(first_name='Bob', last_name="Marley", image_url="https://images.theconversation.com/files/144359/original/image-20161103-25349-1jdv0b3.jpg")
        db.session.add(bob)
        db.session.commit()

        b1 = Post(title='Greatness', content='The greatness of a man is not in how much wealth he acquires, but in his integrity and his ability to affect those around him positively.', user_id=1)
        b2 = Post(title='Happiness', content='Just because you are happy it does not mean that the day is perfect but that you have looked beyond its imperfections.', user_id=1)
        db.session.add(b1)
        db.session.add(b2)
        db.session.commit()

    def tearDown(self):
        """Clean up any fouled transaction."""
        db.session.rollback()
        
    def test_post_details(self):
        with app.test_client() as client:
            resp = client.get('/posts/2')
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('Happiness', html)

    def test_post_edit_form(self):
        with app.test_client() as client:
            resp = client.get('/posts/2/edit')
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('Happiness', html)
            self.assertIn('<h1 class="h1">Edit Post for Bob Marley</h1>', html)
    
    def test_post_delete(self):
        with app.test_client() as client:
            resp = client.post('/posts/1/delete', follow_redirects=True)
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1 class="h1 mt-2">Bob Marley</h1>', html)
            self.assertIn('Happiness', html)
            self.assertNotIn('Greatness', html)


