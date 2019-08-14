import json

with open('../external/city.backup.json', 'r') as dumpFile:
    cityJSON = json.loads(dumpFile.read())


CITY_FIXTURES = []


# city fixture
# [
#     {
#         "model": "city.city",
#         "pk": 1,
#         "fields": {
#             "introduction": "dasda",
#             "district": 15,
#             "sinhalaName": "dsad",
#             "englishName": "sadsa",
#             "tamilName": "sadsad",
#             "area": "sad",
#             "featureImage": "",
#             "mapUrl": "http://localhost:8000/adminpanel/city/create/",
#             "postal_code": null
#         }
#     }
# ]

for city in cityJSON:

    # create newcity object
    newCity = {}

    newCity.setdefault('model', 'city.city')
    newCity.setdefault('pk', city.get('id'))
    newCity.update({
        "fields": {
            "district": 15,
            "sinhalaName": city.get('name_si'),
            "englishName": city.get('name_en'),
            "tamilName": city.get('name_ta'),
            "postal_code": 0 if city.get('postcode') == "" else city.get('postcode')
        }
    })

    # append newly created city objects
    CITY_FIXTURES.append(newCity)

# create new fixure file
with open('../dumps/city.json', 'w') as createJSON:
    createJSON.write(json.dumps(CITY_FIXTURES))
