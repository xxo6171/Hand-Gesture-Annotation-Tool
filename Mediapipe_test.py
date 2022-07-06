import cv2
from cv2 import KeyPoint
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
  
with mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
 
    filename = 'Resource\Image\hand.jpeg'
    image = cv2.imread(filename, cv2.IMREAD_COLOR)
    # image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    results = hands.process(image)

    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow('image', image)
    cv2.waitKey()
    
h, w, c = image.shape

keypoints = []
for data_point in hand_landmarks.landmark:
    keypoints.append({
                         'X': int(data_point.x*w),  # x축에서의 좌표_정규화됨_픽셀 폭으로 나눈 값으로 초기화됨
                         'Y': int(data_point.y*h),  # y축에서의 좌표_정규화됨_픽셀 높이로 나눈 값으로 초기화됨
                        #  'Z': data_point.z,         # z축에서의 좌표_정규화됨_손목을 기준으로 카메라에 가까울수록 값이 작다.
                        #   'Visibility': data_point.visibility,
                         })