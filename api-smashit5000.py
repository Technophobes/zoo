import requests
import json

# r =requests.get("http://127.0.0.1:5000/genus_and_species_and_specimen/6")

# # print(r.text)
# # print(r.json())
# #print(type(r.json()))

# # for i in r.json():
# #     print(i["genus_scientific_name"])

# pload = {"scientific_name":"alien2"}
# g = requests.post("http://127.0.0.1:5000/add_genus" , json = pload)

# print(g.text)



species_list = [
    {"common_name": "Domestic Cat", "scientific_name": "Felis catus", "genus": {"scientific_name": "Felis"} },
    {"common_name": "Black Footed cat", "scientific_name": "Felis nigripes", "genus": {"scientific_name": "Felis"}},
    {"common_name": "Jungle cat", "scientific_name": "Felis chaus", "genus": {"scientific_name": "Felis"}},
    {"common_name": "Domestic Dog", "scientific_name": "Canis familiaris", "genus": {"scientific_name": "Canis"}},
    {"common_name": "Elk", "scientific_name": "Cervus canadensis", "genus": {"scientific_name": "Cervus"}},
    {"common_name": "Giant amoeba", "scientific_name": "Chaos carolinense", "genus": {"scientific_name": "Chaos"}},
    {"common_name": "Common Bottlenose Dolphin", "scientific_name": "Tursiops truncatus", "genus": {"scientific_name": "Tursiops"}},
    {"common_name": "Sea otter", "scientific_name": "Enhydra lutris", "genus": {"scientific_name": "Enhydra"}},
    {"common_name": "Wolf", "scientific_name": "Canis lupus", "genus": {"scientific_name": "Canis"}}
] 

for species in species_list:
    pload = json.dumps(species)
    s = requests.post("http://127.0.0.1:5000/add_species" , json = pload)
    print(species["common_name"])



# def addSpecies(session, species_input):
#     genus = Genus()
#     try: 
#         genus = session.query(Genus).filter(Genus.scientific_name == species_input["genus"]["scientific_name"]).one()
#     except:
#         genus = Genus()
#         genus.scientific_name = species_input["genus"]["scientific_name"]
#         session.add(genus)
#     species = Species()
#     species.scientific_name = species_input["scientific_name"]
#     species.common_name = species_input["common_name"]
#     species.genus = genus
#     session.add(species)
#     session.commit()


# specimen_list = [
#     {"name": "bongo", "species": {"scientific_name": "Felis nigripes"}, "birth_date_time": "1262304000"},
#     {"name": "coco", "species": {"scientific_name": "Cervus canadensis"}, "birth_date_time": "1293840000"},
#     {"name": "lola", "species": {"scientific_name": "Tursiops truncatus"}, "birth_date_time": "1325376000"},
#     {"name": "shadow", "species": {"scientific_name": "Tursiops truncatus"}, "birth_date_time": "1356998400"},
#     {"name": "stella", "species": {"scientific_name": "Enhydra lutris"}, "birth_date_time": "1420070400"}
# ]
