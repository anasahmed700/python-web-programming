# from model import *

# # INSERT query
# flight = Flight(origin="New York", 
#     destination="Paris",
#     duration=540)
# db.session.add(flight)

# # SELECT all query
# Flight.query.all()

#             # WHERE 
# Flight.query.filter_by(origin='Paris').all()

#                                     # LIMIT 1
# Flight.query.filter_by(origin='Paris').first()

#                                     #  COUNT(*)
# Flight.query.filter_by(origin='Paris').count()

#                 # WHERE id = 28
# Flight.query.filter_by(id=28).first()
# Flight.query.get(28)

# # UPDATE duration
# flight =Flight.query.get(3)
# flight.duration = 280

# # DELETE flight
# flight =Flight.query.get(3)
# db.session.delete(flight)

# # COMMIT
# db.session.commit()

# # ORDER_BY
# Flight.query.order_by(flight.origin).all()

# # ORDER_BY DESC (descending order)
# Flight.query.order_by(flight.origin).all()

# # SELECT * FROM flights WHERE origin LIKE "%a%"
# Flight.query.filter(Flight.origin.like("%a%")).all()

# # IN('Tokyo', 'Paris')
# Flight.query.filter(Flight.origin.in_(["Tokyo", "Paris"])).all()

#                     # OR 
# Flight.query.filter(or_(Flight.origin == "Paris", Flight.duration > 500)).all()

#                 # JOIN tables 
# db.session.query(Flight, Passenger).filter(Flight.id == Passenger.flight_id).all()
