import requests
import json


# Shouldn't have IDs in Test Data. The IDs are created when the record is added to the database

# Basic Examples of Using Requests Referenced Here
# r =requests.get("http://127.0.0.1:5000/genus_and_species_and_specimen/6")

# print(r.text)
# print(r.json())
# print(type(r.json()))

# for i in r.json():
#     print(i["genus_scientific_name"])


# pload = {"scientific_name":"alien2"}
# g = requests.post("http://127.0.0.1:5000/add_genus" , json = pload)
# print(g.text)

test_list = [
    {"name": "tubby", "dob": "1262304000", "species_common": "domestic cat", "species_scientific": "felis testus", "genus_scientific": "felis"}, 
    {"name": "batman", "dob": "1262304001", "species_common": "domestic cat", "species_scientific": "felis testus", "genus_scientific": "felis"} 
]

for input_dict in test_list:    
    pload_genus = {"scientific_name": input_dict["genus_scientific"]}
    genus_request = requests.post("http://127.0.0.1:5000/genus" , json=pload_genus)
    genus_id = genus_request.text
    
    pload_species = {"genus_instance": input_dict["species_scientific"]}
    species_request = requests.post("http://127.0.0.1:5000/species" , json=pload_species)
    species_id = species_request.text   
    print(species_id)



# for genus in test_list:
#     pload = {"scientific_name": genus["genus"]}
    # genus_request = requests.post("http://127.0.0.1:5000/genus" , json=pload)
    # genus_id = genus_request.json()

# # for species in test_list:
# pload = test_list["species_scientific"]
# species_request = requests.post("http://127.0.0.1:5000/species" , json=pload)
# species_id = species_request.json()    

# # for specimen in test_list:
# pload = test_list["name"]
# specimen_request = requests.post("http://127.0.0.1:5000/species" , json=pload)
# specimen_id = specimen_request.json()  





# species_list = [
#     {"common_name": "Domestic Cat", "scientific_name": "Felis catus", "genus": {"scientific_name": "Felis"} },
#     {"common_name": "Black Footed cat", "scientific_name": "Felis nigripes", "genus": {"scientific_name": "Felis"}},
#     {"common_name": "Jungle cat", "scientific_name": "Felis chaus", "genus": {"scientific_name": "Felis"}},
#     {"common_name": "Domestic Dog", "scientific_name": "Canis familiaris", "genus": {"scientific_name": "Canis"}},
#     {"common_name": "Elk", "scientific_name": "Cervus canadensis", "genus": {"scientific_name": "Cervus"}},
#     {"common_name": "Giant amoeba", "scientific_name": "Chaos carolinense", "genus": {"scientific_name": "Chaos"}},
#     {"common_name": "Common Bottlenose Dolphin", "scientific_name": "Tursiops truncatus", "genus": {"scientific_name": "Tursiops"}},
#     {"common_name": "Sea otter", "scientific_name": "Enhydra lutris", "genus": {"scientific_name": "Enhydra"}},
#     {"common_name": "Wolf", "scientific_name": "Canis lupus", "genus": {"scientific_name": "Canis"}}
# ] 

# for species in species_list:
#     pload_genus = species["genus"]
#     g = requests.post("http://127.0.0.1:5000/add_genus" , json = pload_genus)
#     pload_species = species
#     s = requests.post("http://127.0.0.1:5000/add_species" , json = pload_species)
# #    print(species["common_name"])




# specimen_list = [
#     {"name": "bongo", "species": {"scientific_name": "Felis nigripes"}, "birth_date_time": "1262304000"},
#     {"name": "coco", "species": {"scientific_name": "Cervus canadensis"}, "birth_date_time": "1293840000"},
#     {"name": "lola", "species": {"scientific_name": "Tursiops truncatus"}, "birth_date_time": "1325376000"},
#     {"name": "shadow", "species": {"scientific_name": "Tursiops truncatus"}, "birth_date_time": "1356998400"},
#     {"name": "stella", "species": {"scientific_name": "Enhydra lutris"}, "birth_date_time": "1420070400"}
# ]

# for specimen in specimen_list: 
#     pload_specimen = specimen
#     sp = requests.post("http://127.0.0.1:5000/add_specimen" , json = pload_specimen)