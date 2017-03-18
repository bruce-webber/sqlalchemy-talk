import sqlite3

# Create a connection and cursor.
conn = sqlite3.connect('roster.db')
c = conn.cursor()

# Create the tables.
c.execute("""
create table person (
    id int primary key not null,
    first_name text,
    last_name text
);
""")
conn.commit()
print('Created the person table')

c.execute("""
create table phone (
    id int primary key not null,
    person_id int not null,
    phone_number text,
    phone_type text
);
""")
conn.commit()
print('Created the phone table')

# Insert the person rows.
c.execute("insert into person (id, first_name, last_name) values (1, 'John', 'Adams')")
c.execute("insert into person (id, first_name, last_name) values (2, 'Richard', 'Recluse')")
c.execute("insert into person (id, first_name, last_name) values (3, 'Sara', 'Smith')")
conn.commit()
print('Inserted people')

# Insert the phone rows.
c.execute("insert into phone (id, person_id, phone_number, phone_type) values (1, 1, '555-1234', 'home')")
c.execute("insert into phone (id, person_id, phone_number, phone_type) values (2, 1, '555-5555', 'cell')")
c.execute("insert into phone (id, person_id, phone_number, phone_type) values (3, 3, '555-9999', 'cell')")
conn.commit()
print('Inserted phone numbers')
