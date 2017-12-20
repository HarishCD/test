import json

with open("file.txt")as json_data:
    jdata = json.load(json_data)
    sdata = json.dumps(jdata)

print sdata

