import json

#python to json

#json.dumps() converts a dictionary to a json object

#creates a python object
dict = {
    "myname" : "Allyson", 
    "day" : 1, 
    "id" : "000851700"
}


#convert to json
jsondata = json.dumps(dict)

print(jsondata)

#for the other way around, use json.loads





