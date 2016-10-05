#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Testing MySQL statements: CREATE TABLE, INSERT and SELECT"""
import MySQLdb

conn = MySQLdb.connect('localhost', 'testuser', '12345678', 'testdb')

with conn:   # Automatically close with error handling
    cursor = conn.cursor()
    # Create a new table
    cursor.execute('drop table if exists cafe')
    cursor.execute('''create table if not exists cafe (
                        id int unsigned not null auto_increment,
                        category enum('tea', 'coffee') not null,
                        name varchar(50) not null,
                        price decimal(5,2) not null,
                        primary key (id)
                      )''')
    # Insert one record
    cursor.execute('''insert into cafe (category, name, price) values
                        ('coffee', 'Espresso', 3.19)''')
    # Insert multiple records
    cursor.execute('''insert into cafe (category, name, price) values
                        ('coffee', 'Cappuccino', 3.29),
                        ('coffee', 'Caffe Latte', 3.39),
                        ('tea', 'Green Tea', 2.99),
                        ('tea', 'Wulong Tea', 2.89)''')
    # Commit the insert
    conn.commit()
    # Query all records
    cursor.execute('select * from cafe')
    # Fetch all rows from result-set into 'a tuple of tuples'
    rows = cursor.fetchall()
    #print(rows)  # For debugging
    # Process each row (tuple)
    for row in rows:
        print(row)
        
    # Instead of fetching all rows (which may not be feasible),
    # we can fetch row by row.
    # We also fetch the column names.
    cursor.execute('select * from cafe')
    # Fetch the column descriptions in 'a tuple of tuples'
    # Each inner tuple describes a column
    desc = cursor.description  
    #print(desc)  # For debugging
    # Print header of column names (first item of inner tuple)
    print('%-10s %-20s %-6s' % (desc[1][0], desc[2][0], desc[3][0]))
    print('%10s-%20s-%6s' % ('-'*10, '-'*20, '-'*6))  # Print divider
    
    for i in range(cursor.rowcount):
        row = cursor.fetchone()
        print('%-10s %-20s %6.2f' % (row[1], row[2], row[3]))  # Using tuple indexes
        
    # Another way to fetch row-by-row
    cursor.execute('select * from cafe')
    while True:
        row = cursor.fetchone()
        if row == None:
            break
        print(row)