import json
import logging
import os

# set up logging configuration
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# create a logger
logger = logging.getLogger(__name__)

# create a dictionary
jsonvar = {
    "broker_address": "localhost",
    "port": 1883,
    "topic": "test/topic"
}

# log the creation of the dictionary
logger.debug("Dictionary created: %s", jsonvar)

def write_json(filename, jsonvar):
    with open(filename, "w") as outfile: # open the file in write mode
        json.dump(jsonvar, outfile)  # write json using json.dump method
    # log that json data has been written to the file
    logger.info("JSON data written to file: %s", filename)
    return True

def read_json(filename):
    with open(filename, 'r') as openfile:  # open the file in read mode
        jsonvar = json.load(openfile)  # read the json data using json.load
    # log that json data has been read from the file
    logger.info("JSON data read from file: %s", filename)
    return jsonvar

# define the filename
filename = 'myjson.json'

# call write_json and read_json functions
write_json(filename, jsonvar)
print(read_json(filename))





