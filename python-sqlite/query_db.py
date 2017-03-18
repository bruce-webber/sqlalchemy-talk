import sqlite3

# Create a connection and cursor.
conn = sqlite3.connect('roster.db')
c = conn.cursor()

# Query for the names and phone numbers.
rows = c.execute("""
select person.first_name, person.last_name, phone.phone_number, phone.phone_type
from person left outer join phone on person.id = phone.person_id
""")

for row in rows:
    print(row)
