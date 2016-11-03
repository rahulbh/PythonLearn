# -*- coding: UTF-8 -*-
"""(sqlalchemy_app2.py) SQLAlchemy Example 2: Using ORM"""
from sqlalchemy import create_engine, Column, Integer, String, Enum, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

# Get the base class of our models
Base = declarative_base()

# Define Object Mapper for table `cafe`
# CREATE TABLE cafe (
#    id INTEGER NOT NULL AUTO_INCREMENT, 
#    category ENUM('tea','coffee'), 
#    name VARCHAR(50), 
#    price NUMERIC(5, 2), 
#    PRIMARY KEY (id)
# )
class Cafe(Base):
   __tablename__ = 'cafe'

   id = Column(Integer, primary_key=True, autoincrement=True)
   category = Column(Enum('tea', 'coffee'))
   name = Column(String(50))
   price = Column(Numeric(precision=5, scale=2))

   def __init__(self, category, name, price, id=None):
      """Constructor"""
      if id:
         self.id = id   # Otherwise, default to auto-increment
      self.category = category
      self.name = name
      self.price = price
      # NOTE: You can use the default constructor,
      #   which accepts all the fields as keyword arguments

   def __repr__(self):
      """Show this object (database record)"""
      return "<Cafe(%d, %s, %s, %5.2f)>" % (
         self.id, self.category, self.name, self.price)

# Create a database engine
engine = create_engine('mysql://testuser:12345678@localhost:3306/testdb')
engine.echo = True  # Echo output to console for debugging

# Drop all tables mapped in Base's subclasses
Base.metadata.drop_all(engine)

# Create all tables mapped in Base's subclasses
Base.metadata.create_all(engine)

# Create a database session binded to our engine, which serves as a staging area
# for changes to the objects. To make persistent changes to database, call
# commit(); otherwise, call rollback() to abort.
Session = scoped_session(sessionmaker(bind=engine))
dbsession = Session()

# Insert one row via add(instance) and commit
# Construct a Cafe instance via the constructor
dbsession.add(Cafe('coffee', 'Espresso', 3.19))
# INSERT INTO cafe (category, name, price) VALUES ('coffee', 'Espresso', 3.19)
dbsession.commit()

# Insert multiple rows via add_all(list_of_instances) and commit
dbsession.add_all([Cafe('coffee', 'Cappuccino', 3.29), 
                 Cafe('tea', 'Green Tea', 2.99, id=8)])  # using kwarg for id
dbsession.commit()

# Select all rows. Return a list of Cafe instances
for instance in dbsession.query(Cafe).all():
   print(instance.category, instance.name, instance.price)
# SELECT cafe.id AS cafe_id, cafe.category AS cafe_category, 
#   cafe.name AS cafe_name, cafe.price AS cafe_price FROM cafe
# ('coffee', 'Espresso', Decimal('3.19'))
# ('coffee', 'Cappuccino', Decimal('3.29'))
# ('tea', 'Green Tea', Decimal('2.99'))

# Select the first row with order_by. Return one instance of Cafe
instance = dbsession.query(Cafe).order_by(Cafe.name).first()
print(instance)   # Invoke __repr__()
# SELECT cafe.id AS cafe_id, cafe.category AS cafe_category, 
#   cafe.name AS cafe_name, cafe.price AS cafe_price 
# FROM cafe ORDER BY cafe.name LIMIT (1,)
# <Cafe(2, coffee, Cappuccino,  3.29)>

# Using filter_by on column
for instance in dbsession.query(Cafe).filter_by(category='coffee').all():
   print(instance.__dict__)   # Print object as key-value pairs
# SELECT cafe.id AS cafe_id, cafe.category AS cafe_category, 
#   cafe.name AS cafe_name, cafe.price AS cafe_price 
# FROM cafe WHERE cafe.category = ('coffee',)

# Using filter with criterion
for instance in dbsession.query(Cafe).filter(Cafe.price < 3).all():
   print(instance)
# SELECT cafe.id AS cafe_id, cafe.category AS cafe_category, 
#   cafe.name AS cafe_name, cafe.price AS cafe_price 
# FROM cafe WHERE cafe.price < (3,)

# Delete rows
instances_to_delete = dbsession.query(Cafe).filter_by(name='Cappuccino').all()
for instance in instances_to_delete:
   dbsession.delete(instance)
dbsession.commit()
# DELETE FROM cafe WHERE cafe.id = (2L,)

for instance in dbsession.query(Cafe).all():
   print(instance)