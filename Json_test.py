import json
'''
test = {
    'shapes': [
        {
            'label': 'test_label',
            'points': [
                [10, 30]
            ],
            'shape_type': 'Line'
        }
    ],
    'image_path': 'Resource\Image\hand.jpeg',
    'image_height': 300,
    'image_width': 300
}
'''
'''
Jason Open
with open('Resource\json\sample_without_image_data.json', 'r') as f:
    json_data = json.load(f)

print(json.dumps(json_data, indent='\t'))
'''

test_dict = {}
test_dict['shapes'] = []
test_dict['image_path'] = 'Resource\Image\hand.jpeg'
test_dict['image_height'] = 300
test_dict['image_width'] = 300

sub_dict = {}
sub_dict['label'] = 'test_label'
sub_dict['points'] = []
sub_dict['points'].append([10, 30])
sub_dict['shape_type'] = 'Line'
test_dict['shapes'].append(sub_dict)

