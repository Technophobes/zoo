
from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import Flask
from flask import jsonify
from flask import request
from model import Species, Specimen, Genus, dbconnect
app = Flask(__name__)

Base = declarative_base()


def addSpecimen(session, specimen_input):
    try:  # Lets check if we can retreive the species matching the specimen record.
        species = session.query(Species).filter(Species.scientific_name == specimen_input["species"]["scientific_name"]).one()
    except:
        species = Species()
        species.scientific_name = specimen_input["species"]["scientific_name"]
        session.add(species)
    specimen = Specimen()
    specimen.name = specimen_input["name"]
    specimen.birth_date_time = specimen_input["birth_date_time"]
    specimen.species = species
    session.add(specimen)
    session.commit()


def addSpecies(session, species_input):
    genus = Genus()
    try: 
        genus = session.query(Genus).filter(Genus.scientific_name == species_input["genus"]["scientific_name"]).one()
    except:
        genus = Genus()
        genus.scientific_name = species_input["genus"]["scientific_name"]
        session.add(genus)
    species = Species()
    species.scientific_name = species_input["scientific_name"]
    species.common_name = species_input["common_name"]
    species.genus = genus
    session.add(species)
    session.commit()




