from flask import Flask , render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from model import *

app = Flask(__name__)
# engine = create_engine("postgresql://postgres:toor@localhost:5432/flightsdb")
# db = scoped_session(sessionmaker(bind=engine))
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:toor@localhost:5432/flight_orm_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.route('/')
def index():
    # flights = db.execute("SELECT * FROM flights").fetchall()
    flights = Flight.query.all()
    return render_template("index.html", flights=flights)

@app.route('/book', methods=["POST"])
def book():
    """Book a flight"""
    #Get form information
    name = request.form.get("name")
    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("error.html", message="Invalid flight number!")

    # make sure the flight exist 
    # if db.execute("SELECT * FROM flights WHERE id = :id", {"id": flight_id}).rowcount == 0: 
    flight = Flight.query.get(flight_id)
    if flight is None:
        return render_template("error.html", message="No such flight with that id.")

    # db.execute("INSERT INTO passengers(name, flight_id) VALUES(:name, :flight_id)",
    #     {"name": name, "flight_id": flight_id})
    # db.commit()
    passenger = Passenger(name=name, flight_id=flight_id)
    db.session.add(passenger)
    db.session.commit()
    return render_template("success.html")

@app.route('/flights')
def flights(): 
    """List all flights."""    
    # flights = db.execute("SELECT * from flights").fetchall()
    flights = Flight.query.all()
    return render_template("flights.html", flights=flights)

@app.route('/flights/<int:flight_id>')
def flight(flight_id):
    """List details about a single flight"""
    # Make sure flight exist
    # flight = db.execute("select * from flights where id = :id", {"id": flight_id}).fetchone()
    flight = Flight.query.get(flight_id)
    if flight is None:
        return render_template("error.html", message="No such flight.")
    
    # Get all passengers
    # passengers = db.execute("select name from passengers where flight_id = :flight_id",
    #     {"flight_id": flight_id}).fetchall()
    passengers = Passenger.query.filter_by(flight_id=flight_id).all()
    return render_template("flight.html", flight=flight, passengers=passengers)
    

# if __name__ == "__main__":
#     main()
