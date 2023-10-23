input = [
        {
            "cell_name": "Living cells",
            "children": [
                {"name": "Events", "value": "7888"},
                {"name": "Parent", "value": "86.7"},
                {"name": "CD38 PE-A Median", "value": "7.1"},
            ]
        }
    ]
import json


counter = 0
while counter < len(input):
    temp = {}
    for obj in input[counter]:
        if obj == 'children':
            for k in input[counter][obj]:
                temp[k['name']] = k['value']
        else:
            temp['cell_name'] = 'asim'
    counter += 1

print(json.dumps(temp, indent=4))