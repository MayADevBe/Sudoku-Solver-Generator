import json
import os.path
import random

def save_field(field):
    fields = load_fields()
    fields.append(field)
    with open("fields.json", 'w') as f:
        json.dump(fields, f)

def load_fields():
    try:
        with open("fields.json", "r") as f:
            fields = json.load(f)     
        return fields
    except:
        with open("fields.json", "w") as f:
            fields = []
            json.dump(fields, f)
    return fields

def get_random_field():
    fields = load_fields()
    if len(fields) > 0:
        r = random.randint(0, len(fields)-1)
        return fields[r]
    else:
        return generate_field()

def generate_field():
    pass