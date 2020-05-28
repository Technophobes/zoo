
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

# to get the error message on the url
if __name__ == '__main__':

    app.run(debug=True)

