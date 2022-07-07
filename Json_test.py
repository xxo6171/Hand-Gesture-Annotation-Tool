import json

test = {
    'shapes': [
        {
            'label': 'test_label',
            'points': [
                [0, 0],
                [1, 1],
                [10, 10]
            ],
            'shape_type': 'Polygon'
        },
        {
            'label': 'test_label',
            'points': [
                [10, 20],
                [17, 5],
                [10, 10]
            ],
            'shape_type': 'Polygon'
        }
    ],
    'image_path': 'Resource\Image\hand.jpeg',
    'image_height': 300,
    'image_width': 300
}

print(test.keys())

# Jason Open
# with open('Resource\json\sample_without_image_data.json', 'r') as f:
#     json_data = json.load(f)

# print(json.dumps(json_data, indent='\t'))