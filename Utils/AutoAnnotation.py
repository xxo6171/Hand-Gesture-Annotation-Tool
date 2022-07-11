import cv2
import mediapipe as mp

def autoAnnotation(img):
    image = img
    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands

    with mp_hands.Hands(
        max_num_hands=1,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:

        results = hands.process(image)

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    return image, hand_landmarks

def landmarksToList(landmarks):
    pos_list = []

    for data_point in landmarks.landmark:
        x_pos = data_point.x
        y_pos = data_point.y
        pos_list.append([x_pos, y_pos])

    return pos_list

'''
if __name__ == '__main__':
    filename = 'Resource\Image\hand.jpeg'
    image = cv2.imread(filename, cv2.IMREAD_COLOR)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    image, landmarks = autoAnnotation(image)
    annotation_dict = landmarksToList(landmarks)

    print(annotation_dict)
    cv2.imshow('image', image)
    cv2.waitKey()
'''