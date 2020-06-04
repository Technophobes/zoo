
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



@app.route('/add_genus', methods=['POST'])
def add_genus():
    session = dbconnect()
    request_dict = request.get_json()
    try: 
        genus_instance = session.query(Genus).filter(Genus.scientific_name == request_dict["scientific_name"]).one()
        return "Genus already exists", 400
    except:
        genus_instance = Genus()
        genus_instance.scientific_name = request_dict["scientific_name"]
        session.add(genus_instance)
        session.commit()
        return "ok"    


@app.route('/add_species',  methods=['POST'])
def add_species():
    session = dbconnect()
    request_dict = request.get_json()
    try:
        genus_instance = session.query(Genus).filter(Genus.scientific_name == request_dict["genus"]["scientific_name"]).one()
    except:
        return "Genus does not exist, please add it", 400
    species = Species() 
    species.scientific_name = request_dict["scientific_name"]
    species.common_name = request_dict["common_name"]
    species.genus_id = genus_instance.id
    session.add(species)
    session.commit()
    return "ok"



@app.route('/add_specimen', methods=['POST'])
def add_specimen(): 
    session = dbconnect()
    request_dict = request.get_json()
    try: 
        species = session.query(Species).filter(Species.scientific_name == request_dict["species"]["scientific_name"]).one() #fix the database table so that there is only one 
    except: 
        return "Species does not exist, please add it", 400
    specimen = Specimen()
    specimen.name = request_dict["name"]
    specimen.birth_date_time = request_dict["birth_date_time"]
    specimen.species_id = species.id    
    session.add(specimen)
    session.commit()
    return "ok"


@app.route('/genus_and_species_and_specimen/<search_term>', methods=['GET'])
def get_genus_and_species_and_specimen(search_term):
    if request.method == 'GET':
        return_list = []
        session = dbconnect()

        
        for genus_instance, species_instance, specimen_instance in session.query(Genus, Species, Specimen).filter(
            Genus.id == search_term, Genus.id == Species.genus_id, Species.id == Specimen.species_id).all():
            
            row = {}
            row["genus_id"] = genus_instance.id
            row["genus_scientific_name"] = genus_instance.scientific_name
            row["species_id"] = species_instance.id
            row["species_scientific_name"] = species_instance.scientific_name
            row["specimen_id"] = specimen_instance.id
            row["specimen_name"] = specimen_instance.name
            return_list.append(row)
        return jsonify(return_list)
    else:
        return "Unsupported Method"

@app.route('/species/<search_term>', methods=['GET'])
def get_species(search_term):
    session = dbconnect()
    return_list = []
    print(search_term)
    for row in session.query(Species).filter(Species.scientific_name == search_term).all():
        row_dict = row.__dict__
        row_dict.pop("_sa_instance_state")
        return_list.append(row_dict)
    return jsonify(return_list)






# to get the error message on the url
if __name__ == '__main__':

    app.run(debug=True)



