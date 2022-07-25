import json
import time

def dict2Json(dict, filepath) :
    with open(filepath, 'w') as f:
        json.dump(dict, f, indent='\t')
    print('Saved file\n' + time.strftime('%c', time.localtime()) + '\n' + filepath + '\n')

def json2Dict(filepath) :
    with open(filepath) as f:
        return json.load(f)