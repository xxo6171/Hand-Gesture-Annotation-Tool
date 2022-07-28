import json
import time

def dict2Json(dict, filepath) :
    with open(filepath, 'w') as f:
        json.dump(dict, f, indent='\t')
    print('Saved file\n' + time.strftime('%c', time.localtime()) + '\n' + filepath + '\n')

def json2Dict(filepath) :
    with open(filepath) as f:
        return json.load(f)

def normalization(annot_dict, w, h):
    shapes = annot_dict['shapes']
    for shape in shapes:
        points = shape['points']
        for point in points:
            point[0] /= w
            point[1] /= h

    return annot_dict

def denormalization(annot_dict, w, h):
    shapes = annot_dict['shapes']
    for shape in shapes:
        points = shape['points']
        for point in points:
            point[0] *= w
            point[1] *= h
            
    return annot_dict