# Tests if there is an error when a duplicate genus, species or specimen is added to the database
# Exit(0) means test is a success

import requests
import json


def genus_request(genus_dict):
    genus_request1 = requests.post("http://127.0.0.1:5000/genus" , json=genus_dict)
    genus_request2 = requests.post("http://127.0.0.1:5000/genus" , json=genus_dict)

    if genus_request1.status_code == 200 and genus_request2.status_code == 400:
        # returns genus ID
        return genus_request1.text
    else:
        print("Something went wrong adding genus")
        exit(1)


def species_request(species_dict):
    species_request1 = requests.post("http://127.0.0.1:5000/species" , json=species_dict)
    species_request2 = requests.post("http://127.0.0.1:5000/species" , json=species_dict)

    if species_request1.status_code == 200 and species_request2.status_code == 400:
        # returns species ID
        return species_request1.text
    else:
        print("Something went wrong adding species")
        exit(1)


def specimen_request(specimen_dict):
    specimen_request1 = requests.post("http://127.0.0.1:5000/specimen" , json=specimen_dict)
    specimen_request2 = requests.post("http://127.0.0.1:5000/specimen" , json=specimen_dict)

    if specimen_request1.status_code == 200 and specimen_request2.status_code == 400:
        # returns specimen ID
        return specimen_request1.text
    else:
        print("Something went wrong with adding specimen")
        exit(1)


genus_dict = {"scientific_name":"panthera"}

genus_id = genus_request(genus_dict)

species_dict = {"common_name": "snow leopard", "scientific_name": "panthera uncia", "genus": {"id": genus_id} }

species_id = species_request(species_dict)

specimen_dict = {"name": "irbis", "species": {"id": species_id}, "birth_date_time": "1262304000"}

specimen_id = specimen_request(specimen_dict)