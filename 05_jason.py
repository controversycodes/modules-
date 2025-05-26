import json

# json.dumps("obj")          #-> Convert dict to JSON string
# json.loads("json_str")     #-> Convert JSON string to dict
# json.dump("obj, file")    # -> Write JSON to file
# json.load("file")         # -> Read JSON from file

data = {'name':'ayaan'}
json_f =json.dumps(data)
print(json_f)


data2 = "syaan"
json_s = json.loads(data)
