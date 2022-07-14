import json

def dict2Json(dict, filepath) :
    with open(filepath, 'w') as f:
        json.dump(dict, f, indent='\t')
    print(filepath)

def json2Dict(filename) :
    pass
