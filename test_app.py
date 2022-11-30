from unittest import TestCase
from app import app
from models import db, User

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
app.config['SQLALCHEMY_ECHO'] = False

app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()

class BloglyTestCase(TestCase):
    """ Tests for Blogly routes. """
    def setUp(self):
        """Add sample user."""
        User.query.delete()

        user = User(first_name="Walter", last_name="Sobchak", image_url='https://pbs.twimg.com/profile_images/986624504616144896/kP8AURXj_400x400.jpg')
        db.session.add(user)
        db.session.commit()

        self.user_id = user.id

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
            self.assertIn('<h1 class="h1">Walter Sobchak</h1>', html)

    def test_user_delete(self):
        with app.test_client() as client:
            resp = client.post('/users/1/delete', follow_redirects=True)
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1 class="h1">Users</h1>', html)
            self.assertNotIn('<li>', html)
            self.assertNotIn('Walter Sobchak', html)