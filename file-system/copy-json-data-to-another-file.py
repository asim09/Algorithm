import json


def writeToJSONFile(fileName, data):
    print(data)
    with open('testing.json') as f:
        json_decoded = json.load(f)
        print(json_decoded)
        for data_key in data.keys():
            if data_key in json_decoded.keys():
                print(data_key, ' --> hai cache mein')
            else:
                print('----enter--')
                json_decoded.update(data)
                with open(fileName, 'w') as fp:
                    json.dump(json_decoded, fp)

data = {}
data['name4'] = 'shubham'
data['name5'] = 'shubham'

writeToJSONFile('testing.json',data)
