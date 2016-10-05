#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Using SQL Prepared-Statement"""
import MySQLdb

conn = MySQLdb.connect('localhost', 'testuser', '12345678', 'testdb')

with conn:
    cursor = conn.cursor()
    cursor.execute('drop table if exists cafe')
    cursor.execute('''create table if not exists cafe (
                        id int unsigned not null auto_increment,
                        category enum('tea', 'coffee') not null,
                        name varchar(50) not null,
                        price decimal(5,2) not null,
                        primary key (id)
                      )''')

    # Using prepared-statement via printf formatting specifiers
    # Use %s for all fields?!
    sql = 'insert into cafe (category, name, price) values (%s, %s, %s)'
    
    # Execute for one set of data
    cursor.execute(sql, ('coffee', 'Espresso', 3.19))
                   
    # Execute for more than one set of data
    data = [('coffee', 'Cappuccino', 3.29),
            ('coffee', 'Caffe Latte', 3.39),
            ('tea', 'Green Tea', 2.99),
            ('tea', 'Wulong Tea', 2.89)]
    cursor.executemany(sql, data)
    conn.commit()  # Commit the insert
    
    cursor.execute('select * from cafe')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Another example
    item = 'Cappuccino'
    cursor.execute('update cafe set price = price * 1.1 where name = %s', item)
    cursor.execute('select * from cafe where name = %s', item)
    row = cursor.fetchone()
    print(row)