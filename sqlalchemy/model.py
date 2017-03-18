from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

# Database model.

Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    def __repr__(self):
        return "<Person(name='{} {}')".format(self.first_name, self.last_name)


class Phone(Base):
    __tablename__ = 'phone'

    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'))
    phone_number = Column(String)
    phone_type = Column(String)

    person = relationship('Person', back_populates='phones')

    def __repr__(self):
        return "<Phone(number='{}')".format(self.phone_number)

Person.phones = relationship('Phone', back_populates='person')
