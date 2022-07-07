from operator import index
import cv2
from cv2 import KeyPoint
import mediapipe as mp

# 제스쳐 포인트 인식 및 출력
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

index_pos = 0
with mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
 
    filename = 'Resource\Image\hand.jpeg'
    image = cv2.imread(filename, cv2.IMREAD_COLOR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    results = hands.process(image)

    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow('image', image)
    cv2.waitKey()


# 포인트 별 레이블 이름 리스트
pos_mapping_list = [
                        'Wrist', 
                        'Thumb_CMC', 'Thumb_MCP','Thumb_IP', 'Thumb_TIP', 
                        'Index_Finger_MCP', 'Index_Finger_PIP', 'Index_Finger_DIP', 'Index_Finger_TIP', 
                        'Middle_Finger_MCP', 'Middle_Finger_PIP', 'Middle_Finger_DIP', 'Middle_Finger_TIP', 
                        'Ring_Finger_MCP', 'Ring_Finger_PIP', 'Ring_Finger_DIP', 'Ring_Finger_TIP',
                        'Pinky_MCP', 'Pinky_PIP', 'Pinky_DIP', 'Pinky_TIP'
                    ]

# 기본 구조 생성
h, w, c = image.shape

test_dict = {}
test_dict['shapes'] = []
test_dict['image_path'] = 'Resource\Image\hand.jpeg'
test_dict['image_height'] = h
test_dict['image_width'] = w

sub_dict = {}
sub_dict['label'] = 'Hand Gesture'
sub_dict['points'] = []
sub_dict['shape_type'] = 'Gesture Poligon'

test_dict['shapes'].append(sub_dict)

# 좌표 정보 입력
index_pos = 0
for data_point in hand_landmarks.landmark:
    sub_point = {}
    sub_point[pos_mapping_list[index_pos]] = [int(data_point.x*w), int(data_point.y*h)]
    sub_dict['points'].append(sub_point)
    index_pos = index_pos + 1

'''
h, w, c = image.shape

keypoints = []
for data_point in hand_landmarks.landmark:
    keypoints.append({
                         'X': int(data_point.x*w),  # x축에서의 좌표_정규화됨_픽셀 폭으로 나눈 값으로 초기화됨
                         'Y': int(data_point.y*h),  # y축에서의 좌표_정규화됨_픽셀 높이로 나눈 값으로 초기화됨
                        #  'Z': data_point.z,         # z축에서의 좌표_정규화됨_손목을 기준으로 카메라에 가까울수록 값이 작다.
                        #   'Visibility': data_point.visibility,
                         })
'''