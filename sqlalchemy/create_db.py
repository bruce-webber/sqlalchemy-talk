from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from model import Person, Phone, Base

# Create the database engine and session.
engine = create_engine('sqlite:///roster.db')
Session = sessionmaker(bind=engine)
session = Session()

# Create the database.
Base.metadata.create_all(engine)

# John Adams
person = Person(first_name='John', last_name='Adams')
phone = Phone(phone_number='555-1234', phone_type='home')
person.phones.append(phone)
phone = Phone(phone_number='555-5555', phone_type='cell')
person.phones.append(phone)
session.add(person)

# Sara Smith
person = Person(first_name='Sara', last_name='Smith')
phone = Phone(phone_number='555-9999', phone_type='cell')
person.phones.append(phone)
session.add(person)

# Richard Recluse
person = Person(first_name='Richard', last_name='Recluse')
session.add(person)

# Commit the records to the database.
session.commit()
