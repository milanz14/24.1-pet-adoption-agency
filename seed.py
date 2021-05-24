from models import Pet, db
from app import app

# create all tables and seed the data
db.drop_all()
db.create_all()

p1 = Pet(name="Spot", species="Terrier")
p2 = Pet(name="Charlie", species="Chihuahua", photo_url='https://images.unsplash.com/photo-1537151625747-768eb6cf92b2?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=932&q=80', age=3, available=False)

db.session.add(p1)
db.session.add(p2)

db.session.commit()
