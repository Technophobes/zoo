
from flask import Flask
from flask import jsonify
from flask import request
from model import dbconnect, Species, Specimen, Genus

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

@app.route('/add_specimen', methods=['POST'])
def add_specimen(): 
    session = dbconnect()
    request_dict = request.get_json()
    specimen = Specimen()
    species = session.query(Species).filter(Species.scientific_name == request_dict["species"]["scientific_name"]).one() #fix the database table so that there is only one 
    specimen.name = request_dict["name"]
    specimen.birth_date_time = request_dict["birth_date_time"]
    specimen.species_id = species.id    
    session.add(specimen)
    session.commit()
    return "ok"

# to get the error message on the url
if __name__ == '__main__':

    app.run(debug=True)

