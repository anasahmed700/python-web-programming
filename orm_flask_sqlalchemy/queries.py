from model import *

# INSERT query
flight = Flight(origin="New York", 
    destination="Paris",
    duration=540)
db.session.add(flight)

# SELECT all query
Flight.query.all()

            # WHERE 
Flight.query.filter_by(origin='Paris').all()

