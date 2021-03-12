# from sqlalchemy import create_engine
# from sqlalchemy import Column, Float, String, Integer, UniqueConstraint
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from os import environ

# db_string = environ['POSTGRES_DB_URL']

# db = create_engine(db_string)
# base = declarative_base()

# class Bike(base):
#     __tablename__ = 'biking_stats'

#     id = Column(Integer, primary_key=True)
#     trip_id = Column(String)
#     start_time = Column(TimeStamp)
#     stop_time = Column(TimeStamp)
#     bike_id = Column(String)
#     from_station_id = Column(String)
#     from_station_name = Column(String)
#     to_station_id = Column(String)
#     to_station_name = Column(String)
#     user_type = Column(String)
#     gender = Column(String)
#     birth_date = Column(DateTime)
#     trip_duration = column(Integer)

    
