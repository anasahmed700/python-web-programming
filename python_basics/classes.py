class Flight: 
    counter = 1
    def __init__(self, origin, destination, duration):
        # keep track of id number 
        self.id = Flight.counter
        Flight.counter += 1

        # keep track of passengers
        self.passengers = []

        # Details about flight
        self.origin = origin
        self.destination = destination
        self.duration = duration

    # custom methods 
    def print_info(self):
        # flight details to display
        print("\nOrigin: ", self.origin)
        print("Destination", self.destination)
        print(f"Duration {self.duration} minutes")
        print("Passengers:")
        for passenger in self.passengers: 
            print(f"{passenger.name}")
    
    def delay(self, mins):
        self.duration += mins

    def add_passenger(self, p):
        self.passengers.append(p)
        p.flight_id = self.id

class Passenger:
    def __init__(self, name):
        self.name = name

def main():
    # Create Flight
    f1 = Flight(origin="Karachi", destination="Makkah", duration=350)
    f2 = Flight("Dhaka", "Istanbul", 250)
    
    # create passengers
    john = Passenger(name="John")
    akbar = Passenger("Akbar")
    ali = Passenger("Ali")
    usman = Passenger("Usman")

    # add passengers to flight    
    f1.add_passenger(john)
    f1.add_passenger(akbar)
    f1.print_info()
    f2.add_passenger(ali)
    f2.add_passenger(usman)

    # change delay value 
    f2.delay(10)
    f2.print_info()


    

# if running this file, than call main()
if __name__ == "__main__":
    main()