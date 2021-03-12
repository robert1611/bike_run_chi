from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api, Resource, reqparse
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import extract

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:robert1972@localhost:5432/bike_api"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
api = Api(app)

db = SQLAlchemy(app)
migrate = Migrate(app,db)

base = declarative_base()

bike_parser = reqparse.RequestParser()
bike_parser.add_argument('start_time')
bike_parser.add_argument('stop_time')

class Bike3(db.Model):
    __tablename__ = 'bike3'

    id = db.Column(db.Integer, primary_key=True)
    trip_id = db.Column(db.String)
    start_time = db.Column(db.TIMESTAMP)
    stop_time = db.Column(db.TIMESTAMP)
    bike_id = db.Column(db.String)
    from_station_id = db.Column(db.String)
    from_station_name = db.Column(db.String)
    to_station_id = db.Column(db.String)
    to_station_name = db.Column(db.String)
    user_type = db.Column(db.String)
    gender = db.Column(db.String)
    birth_date = db.Column(db.String)
    trip_duration = db.Column(db.Integer)

Session = sessionmaker(db)
session = Session()

#base.metadata.create_all(db)

class BikeResource(Resource):
    def get(self):
        return {'hello': 'world'}

    #@jwt_required
    def post(self):
        args = bike_parser.parse_args()
        start_time = args['start_time']
        stop_time = args['stop_time']
        
        avg_minutes = db.session.query(func.avg(func.trunc((extract('epoch', Bike3.stop_time)-extract('epoch', Bike3.start_time)) / 60))).filter(Bike3.start_time>=start_time, Bike3.stop_time<=stop_time).first()[0]


        result = {
            'avg_minutes': avg_minutes
        }
        print(result)
        return jsonify(result)

api.add_resource(BikeResource, '/bike')

@app.route('/')
def hello():
    return ('me and my sons Nicholas and Charles')

if __name__ == '__main__':
    app.run(debug = True)



