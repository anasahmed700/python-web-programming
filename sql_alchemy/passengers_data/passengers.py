
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql://postgres:toor@localhost:5432/flightsdb")
db = scoped_session(sessionmaker(bind=engine))

def main():
    # list all flights
    flights = db.execute("SELECT id, origin, destination, duration FROM flights")
    for flight in flights:
        print(f"Flight {flight.id}: {flight.origin} to {flight.destination}, in {flight.duration} minutes.")
    
    # Prompt user to choose a flight
    flight_id = int(input("\nFlight ID: "))
    flight = db.execute("SELECT origin, destination, duration FROM flights WHERE id = :id",
        {"id": flight.id}).fetchone()
    
    # Make sure flight is valid
    if flight is None: 
        print("Error: No such flight.")
        return
    
    #list passengers
    q = "SELECT name FROM passengers WHERE flight_id = :flight_id"
    params = {"flight_id": flight_id}
    passengers = db.execute(q, params).fetchall()
    print("\nPassengers:")
    for passenger in passengers:
        print(passenger.name)
    if len(passengers) == 0:
        print("No passengers.")

if __name__ == "__main__":
    main()
