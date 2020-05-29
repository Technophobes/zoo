
from flask import Flask
from flask import jsonify
from flask import request
from model import dbconnect, Species, Specimen, Genus
from data import species_list

app = Flask(__name__)

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

@app.route('/species/<search_term>', methods=['GET'])
def get_species(search_term):
    session = dbconnect()
    if request.method == 'GET':
        return_list = []
        print(search_term)
        for species in session.query(Species).filter(Species.id == search_term).all():
            row_dict = row.__dict__
            row_dict.pop("_sa_instance_state")
            return_list.append(row_dict)
        return jsonify(return_list)


@app.route('/species2/<search_term>', methods=['GET'])
def search_species(search_term):
    if request.method == 'GET':
        return_list = []
        session = dbconnect()
        print(search_term)
        for species in session.query(Species).filter(
            Genus.id == search_term, 
            Genus.id == Species.genus_id).all():
            row = {} 
            row["genus_id"] = genus.id
            row["genus_scientific_name"] = genus.scientific_name
            row["species_id"] = species.id
            row["species_scientific_name"] = species.scientific_name
            return_list.append(row)
        return jsonify(return_list)
    else:
        return "Unsupported Method"

# to get the error message on the url
if __name__ == '__main__':

    app.run(debug=True)


