from flask import Flask, request
import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.sql import text
from custom_logger import logger
import os

# Initialize flask-sqlalchemy
class Base(DeclarativeBase):
  pass
db = SQLAlchemy(model_class=Base)

# create the app
app = Flask(__name__)

# Setup sql connection
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"mysql+mysqlconnector://"
    f"{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}"
    f"@{os.getenv('MYSQL_HOST')}/{os.getenv('MYSQL_DATABASE')}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Setup db model
class Countries(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(200), nullable=False)
    c_population = db.Column(db.Integer)
    gdp = db.Column(db.Float)
    debt = db.Column(db.Float)


def check_db_connection():
    try:
        db.session.execute(text('SELECT 1'))
        logger.info("Database connection successful.")
    except Exception as e:
        logger.error("Database connection failed.")
        logger.exception(e)
        raise e


@app.route('/list_countries', methods=['GET'])
def get_countries():
    results = Countries.query.distinct(Countries.country).all()
    return json.dumps([{'country': x.country} for x in results])

@app.route('/country_data', methods=['GET'])
def get_country_data():
    results = Countries.query.all()
    return json.dumps([{'country': x.country, 'population': x.c_population, 'gdp': x.gdp, 'debt': x.debt} for x in results])

if __name__ == '__main__':
    with app.app_context():
        try:
            db.create_all()
            logger.info("Database tables created successfully.")
        except Exception as e:
            logger.error("Error creating database tables.")
            logger.exception(e)
            raise e
        
        check_db_connection()
    app.run(host='0.0.0.0', port=os.getenv('API_PORT'), debug=True)