import json
from turtle import position
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

pos_mapping_list = [
                        'Wrist', 
                        'Thumb_CMC', 'Thumb_MCP','Thumb_IP', 'Thumb_TIP', 
                        'Index_Finger_MCP', 'Index_Finger_PIP', 'Index_Finger_DIP', 'Index_Finger_TIP', 
                        'Middle_Finger_MCP', 'Middle_Finger_PIP', 'Middle_Finger_DIP', 'Middle_Finger_TIP', 
                        'Ring_Finger_MCP', 'Ring_Finger_PIP', 'Ring_Finger_DIP', 'Ring_Finger_TIP',
                        'Pinky_MCP', 'Pinky_PIP', 'Pinky_DIP', 'Pinky_TIP'
                    ]

# 기본 구조 생성
test_dict = {}
test_dict['shapes'] = []
test_dict['image_path'] = 'Resource\Image\hand.jpeg'
test_dict['image_height'] = 300
test_dict['image_width'] = 300

sub_dict = {}
sub_dict['label'] = 'Hand Gesture'
sub_dict['points'] = []
sub_dict['shape_type'] = 'Gesture Poligon'
test_dict['shapes'].append(sub_dict)

# 좌표 정보 입력
sub_point = {}
for index_pos in range(len(pos_mapping_list)):
    sub_point[pos_mapping_list[index_pos]] = [10, 10]
sub_dict['points'].append(sub_point)

print(len(pos_mapping_list))
# print(test_dict)