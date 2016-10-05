#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Using Dictionary Cursor"""
import MySQLdb

conn = MySQLdb.connect('localhost', 'testuser', '12345678', 'testdb')

with conn:
    # Using a dictionary cursor.
    # Each row of the result-set is a dictionary of column names and values
    cursor = conn.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('drop table if exists cafe')
    cursor.execute('''create table if not exists cafe (
                     id int unsigned not null auto_increment,
                     category enum('tea', 'coffee') not null,
                     name varchar(50) not null,
                     price decimal(5,2) not null,
                     primary key (id)
                   )''')
    cursor.execute('''insert into cafe (category, name, price) values
                     ('coffee', 'Espresso', 3.19),
                     ('coffee', 'Cappuccino', 3.29),
                     ('coffee', 'Caffe Latte', 3.39),
                     ('tea', 'Green Tea', 2.99),
                     ('tea', 'Wulong Tea', 2.89)''')
    conn.commit()  # Commit the insert

    # Query all records
    cursor.execute('select * from cafe')
    # Fetch all rows from result-set into 'a tuple of dictionary'
    rows = cursor.fetchall()
    print(rows)  # For debugging
    # Process each row (dictionary)
    for row in rows:
        #print(row)  # For debugging
        print(row['category'] + ': ' + row['name'])  # via dictionary keys