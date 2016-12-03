#!/usr/bin/python

import jsonschema
import simplejson

def validateSchema(tmp):
        # Read data from schema.json
        with open('schema.json') as schemaFile:
                schema = schemaFile.read()

        # Read data from payload.json
        with open(tmp + 'payload.json') as dataFile:
                data = dataFile.read()

        try:
                jsonschema.validate(simplejson.loads(data), simplejson.loads(schema))
                print("PASSED")
        except jsonschema.ValidationError as e:
                print("FAILED")
                print e.message

