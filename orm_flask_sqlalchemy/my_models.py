from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Flight(db.Model):
    __tablename__ = "flights"
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String, nullable=False)
    destination = db.Column(db.String, nullable=False)
    duration = db.Column(db.Integer, nullable=False)


class Passenger(db.Model):
    __tablename__ = "passengers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    flight_id = db.Column(db.Integer, db.ForeignKey('flights.id'), nullable=False)


# INSERT INTO flights
#     (origin, destination, duration)
#     VALUES ('New York', 'Paris', 540)

# flight = Flight(origin="New York",
#                 destination="Paris",
#                 duration=540)
# db.session.add(flight)
#
# # SELECT * FROM flights;
# Flight.query.all()
#
# # SELECT * FROM flights WHERE origin = 'Paris';
# Flight.query.filter_by(origin="Paris").all()


