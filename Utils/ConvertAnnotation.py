import json

def dict2Json(dict, filepath) :
    with open(filepath, 'w') as f:
        json.dump(dict, f, indent='\t')
    print(filepath)

def json2Dict(filepath) :
    with open(filepath) as f:
        dict = json.load(f)
    return dict
