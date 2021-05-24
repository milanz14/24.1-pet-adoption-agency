from unittest import TestCase
from app import app
from models import db, Pet

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_adoption_agency_test'

db.drop_all()
db.create_all()

class TestPetsApp(TestCase):
    """ tests all of the pet agency routes """

    def setUp(self):
        """ clean up existing pets in DB """
        Pet.query.delete()
        test_pet = Pet(name='Test Pet', species='Dog', age=5)
        db.session.add(test_pet)
        db.session.commit()
        self.pet = test_pet
        self.petid = test_pet.id

    def tearDown(self):
        """ clean up any issues with the test DB """
        db.session.rollback()

    def test_show_route(self):
        with app.test_client() as client:
            resp = client.get('/')
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h1 class='title'>Pets :)</h1>", html)
    
    def test_add_pet(self):
        """ tests adding a new pet to the DB """
        with app.test_client() as client:
            d = {"name":"Test Pet", "species":"Dog", "age":10}
            resp = client.post('/add', data=d, follow_redirects=True)

    def test_show_pet_details(self):
        """ tests the pet details page """
        with app.test_client() as client:
            resp = client.get(f'/{self.petid}')
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn("<a href='/' class='button'>Back to Pets Home</a>", html)
    
    