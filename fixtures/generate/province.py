import json
import os

# open backup json file
with open('../external/provinces.backup.json', 'r') as jsonFile:
    data = jsonFile.read()

# convert json to python datastructure -> [{}, {}]
province_old_data = json.loads(data)

# new collection
province_new_data = []

for province in province_old_data:

    # init dictironry / object
    new_province = {}

    # update object
    new_province.update(model="Province.province")
    new_province.update(pk=province.get('id'))
    new_province.update({
        'fields': {
            "sinhalaName": province.get('name_si'),
            "englishName": province.get('name_en'),
            "tamilName": province.get('name_ta')
        }
    })

    # add newly created province obj
    province_new_data.append(new_province)

# create new fixture
with open('../dumps/province.json', 'w') as newJsonFile:

    print(newJsonFile)
    newJsonFile.write(json.dumps(province_new_data))
