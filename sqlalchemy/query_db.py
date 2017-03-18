from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from model import Person

# Create the database engine and session.
engine = create_engine('sqlite:///roster.db')
Session = sessionmaker(bind=engine)
session = Session()

for person in session.query(Person).order_by(Person.last_name):
    print('{} {}'.format(person.first_name, person.last_name))
    for phone in person.phones:
        print('    {} ({})'.format(phone.phone_number, phone.phone_type))
