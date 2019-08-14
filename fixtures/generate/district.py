import json

# open backup json file
with open('../external/districts.backup.json', 'r') as jsonFile:
    data = jsonFile.read()

# convert json to python datastructure -> [{}, {}]
district_old_data = json.loads(data)

# new collection
distrcit_new_data = []

for district in district_old_data:

    # init dictironry / object
    new_district = {}

    # update object
    new_district.update(model="district.district")
    new_district.update(pk=district.get('id'))
    new_district.update({
        'fields': {
            "sinhalaName": district.get('name_si'),
            "englishName": district.get('name_en'),
            "tamilName": district.get('name_ta'),
            "province": district.get('province_id')
        }
    })

    # add newly created province obj
    distrcit_new_data.append(new_district)

# create new fixture
with open('../dumps/district.json', 'w') as newJsonFile:

    newJsonFile.write(json.dumps(distrcit_new_data))
