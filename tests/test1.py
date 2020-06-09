# Test that there is indeed an error when a duplicate is added (identical genus, species and specimen name)
# Duplicate should not be added to the database
# Expected output: In Terminal "already exists" (referring to the 2nd dictionary in test_list) and 1 entry for "irbis" added to DB

import requests
import json

test_list = [
    {"name": "irbis", "dob": "1362304000", "species_common": "snow leopard", "species_scientific": "panthera uncia", "genus_scientific": "panthera"}, 
    {"name": "irbis", "dob": "1362304000", "species_common": "snow leopard", "species_scientific": "panthera uncia", "genus_scientific": "panthera"} 
]

for input_dict in test_list:    
    pload_genus = {"scientific_name": input_dict["genus_scientific"]}
    genus_request = requests.post("http://127.0.0.1:5000/genus" , json=pload_genus)
    genus_id = genus_request.text
    print(genus_id)
    
    if genus_request.status_code == 200: 
        pload_species = {"scientific_name": input_dict["species_scientific"], "common_name" : input_dict["species_common"], "genus" : { "id" : genus_id}}
        species_request = requests.post("http://127.0.0.1:5000/species" , json=pload_species)
        species_id = species_request.text   
        print(species_id)
    else :
        exit(1)

    if species_request.status_code == 200:
        pload_specimen = {"name": input_dict["name"], "birth_date_time" : input_dict["dob"], "species" : {"id" : species_id}}
        specimen_requests = requests.post("http://127.0.0.1:5000/specimen" , json=pload_specimen)
    
    else:
        exit(1)