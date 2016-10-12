# -*- coding: UTF-8 -*-
"""(sqlalchemy_app1.py) SQLAlchemy Example 1: Testing with MySQL"""
from sqlalchemy import create_engine
engine = create_engine('mysql://testuser:12345678@localhost:3306/testdb')

engine.echo = True  # Echo output to console

# Create a database connection
conn = engine.connect()
conn.execute('DROP TABLE IF EXISTS cafe')
conn.execute('''CREATE TABLE IF NOT EXISTS cafe (
                  id INT UNSIGNED NOT NULL AUTO_INCREMENT,
                  category ENUM('tea', 'coffee') NOT NULL,
                  name VARCHAR(50) NOT NULL,
                  price DECIMAL(5,2) NOT NULL,
                  PRIMARY KEY(id)
                )''')

# Insert one record
conn.execute('''INSERT INTO cafe (category, name, price) VALUES
                  ('coffee', 'Espresso', 3.19)''')

# Insert multiple records
conn.execute('''INSERT INTO cafe (category, name, price) VALUES
                  ('coffee', 'Cappuccino', 3.29),
                  ('coffee', 'Caffe Latte', 3.39),
                  ('tea', 'Green Tea', 2.99),
                  ('tea', 'Wulong Tea', 2.89)''')

# Query table
for row in conn.execute('SELECT * FROM cafe'):
    print(row)

# give connection back to the connection pool
conn.close()