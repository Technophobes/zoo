from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import Flask
from flask import jsonify
from flask import request
app = Flask(__name__)

Base = declarative_base()


@app.route('/cool')
def cool():
    session = dbconnect()
    specimens = session.query(Specimen).all()
    # Serialisation starts here
    row_list = []
    for specimen in specimens:
        row_dict = {}
        row_dict["name"] = specimen.name
        row_dict["birth_date_time"] = specimen.birth_date_time
        row_list.append(row_dict)
    return jsonify(row_list)
